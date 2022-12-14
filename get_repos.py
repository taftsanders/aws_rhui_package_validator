import os
import urllib3
import get_links as gl
import get_mirrors as gm
import warnings
warnings.simplefilter('ignore', urllib3.exceptions.SecurityWarning)

RHEL5_RELEASES = ['5.6', '5.7', '5.8', '5.9', '5.10', '5.11'] # curl -s  https://cdn.redhat.com/content/dist/rhel/rhui/server/5/ --cacert /etc/rhsm/ca/redhat-uep.pem --cert cdncert.pem | grep HREF | cut -d'=' -f4 | cut -d'"' -f2 | cut -d'/' -f1 | grep -v listing | grep -v '\.\.'
RHEL5_ARCH = ['i386'] # if release=5.11: arch =[i386,x86_64]
RHEL6_RELEASES = ['6.10', '6Server'] # curl -s https://cdn.redhat.com/content/dist/rhel/rhui/server/6/ --cacert /etc/rhsm/ca/redhat-uep.pem --cert cdncert.pem | grep HREF | cut -d'=' -f4 | cut -d'"' -f2 | cut -d'/' -f1 | grep -v listing | grep -v '\.\.'
RHEL6_ARCH = ['i386', 'x86_64']
RHEL7_RELEASES = ['7.0', '7.1', '7.2', '7.3', '7.4', '7.5', '7.6', '7.7', '7.8'] # curl -s https://cdn.redhat.com/content/dist/rhel/rhui/server/7/ --cacert /etc/rhsm/ca/redhat-uep.pem --cert cdncert.pem | grep HREF | cut -d'=' -f4 | cut -d'"' -f2 | cut -d'/' -f1 | grep -v listing | grep -v '\.\.'
RHEL7_ARCH = ['x86_64']
RHEL8_RELEASES = ['8'] # curl -s  https://cdn.redhat.com/content/dist/rhel8/rhui/ --cacert /etc/rhsm/ca/redhat-uep.pem --cert cdncert.pem | grep HREF | cut -d'=' -f4 | cut -d'"' -f2 | grep -v 'listing' | grep -v '\.'
RHEL8_ARCH = ['aarch64', 'ppc64le', 's390x', 'x86_64'] # curl -s  https://cdn.redhat.com/content/dist/rhel8/rhui/8 --cacert /etc/rhsm/ca/redhat-uep.pem --cert cdncert.pem | grep HREF | cut -d'=' -f4 | cut -d'/' -f2 | grep -v '\.\.'

RHEL6_CERTS = '/tmp/rhui-client-rpms/rhel6/certs'
RHEL7_CERTS = '/tmp/rhui-client-rpms/rhel7/certs'
RHEL8_CERTS = '/tmp/rhui-client-rpms/rhel8/certs'

def replace_region(key, value, region):
    if 'REGION' in value or 'REGION' in key:
        url = value.replace('REGION', region)
        name = key.replace('REGION', region)
    else:
        url = value
        name = key
    return name, url

def replace_basearch(key, value, arch):
    if '$basearch' in value or '$basearch' in key:
        url = value.replace('$basearch', arch)
        name = key.replace('$basearch', arch)
    else:
        url = value
        name = key 
    return name, url

def replace_releasever(key, value, release):
    if '$releasever' in value or '$releasever' in key:
        url = value.replace('$releasever', release)
        name = key.replace('$releasever', release)
    else:
        url = value
        name = key
    return name, url

'''
step 1: region
step 2: repo
step 3: arch
step 4: release version
'''
def get_rhel6_repos():
    gm.get_rhel6_mirror_list()
    rhel6_mirrors = []
#    regions = gl.get_regions()
    regions = ['us-east-1','us-east-1','us-east-1'] # For faster testing, REMOVE ME FOR PROD
    for region in regions[:len(regions)-2]:
        for repo_mirror in gm.rhel6_filtered_repo_mirror:
            name, values = list(repo_mirror.items())[0]
            if (os.path.exists(RHEL6_CERTS + values['sslcacert']) and
                 os.path.exists(RHEL6_CERTS + values['sslclientcert']) and 
                 os.path.exists(RHEL6_CERTS + values['sslclientkey'])):
                req = urllib3.PoolManager(
                    cert_reqs = 'CERT_REQUIRED',
                    ca_certs = RHEL6_CERTS + values['sslcacert'],
                    cert_file = RHEL6_CERTS + values['sslclientcert'],
                    key_file = RHEL6_CERTS + values['sslclientkey'],
                )
            else:
                req = urllib3.PoolManager(
                    cert_reqs = 'CERT_REQUIRED',
                    ca_certs = RHEL6_CERTS + '/etc/pki/rhui/cdn.redhat.com-chain.crt',
                    cert_file = RHEL6_CERTS + '/etc/pki/rhui/product/content-rhel6.crt',
                    key_file = RHEL6_CERTS + '/etc/pki/rhui/content-rhel6.key',
                )
            name1, url1 = replace_region(name, values['mirrorlist'], region)
            for arch in RHEL6_ARCH:
                name2, url2 = replace_basearch(name1, url1, arch)
                for release in RHEL6_RELEASES:
                    name3, url3 = replace_releasever(name2, url2, release)
                    repo = {}
                    baserepo = req.request('GET', url3).data.decode('utf-8')
                    custom_name3 = name3 + '|' + arch + '|' + release
                    repo[custom_name3] = {}
                    repo[custom_name3]['mirrorlist'] = url3
                    repo[custom_name3]['sslcacert'] = values['sslcacert']
                    repo[custom_name3]['sslclientcert'] = values['sslclientcert']
                    repo[custom_name3]['sslclientkey'] = values['sslclientkey']
                    #It would be nice to have cds1 in [0] and cds2 in [1] for all lists
                    repo[custom_name3]['baseurl'] = baserepo.split('\n')
                    print('Getting mirror list for: ' + custom_name3)
                    rhel6_mirrors.append(repo)
    #print(len(rhel6_mirrors)) #DEBUG
    return rhel6_mirrors

if __name__ == "__main__":
    gm.get_rhel6_mirror_list()
#    gm.get_rhel7_mirror_list()
#    gm.get_rhel8_mirror_list()
    print(get_rhel6_repos())