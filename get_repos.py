import urllib3
import get_links as gl
import get_mirrors as gm
import warnings
warnings.simplefilter('ignore', urllib3.exceptions.SecurityWarning)


RHEL6_RELEASES = ['6.10', '6Server']
RHEL6_ARCH = ['i386', 'x86_64']
RHEL7_RELEASES = ['7.3', '7.4', '7.5', '7.6', '7.7', '7.8']
RHEL7_ARCH = ['x86_64']
RHEL8_RELEASES = ['8']
RHEL8_ARCH = ['aarch64', 'ppc64le', 's390x', 'x86_64']

def call_repo_url(repo_name, mirror_url):
    req = urllib3.PoolManager(
        cert_reqs = 'CERT_REQUIRED',
        ca_certs='/tmp/rhui-client-rpms/rhui-ca.crt',
#        )
        cert_file = '/tmp/rhui-client-rpms/master-content-cert.crt',
        key_file = '/tmp/rhui-client-rpms/master-content-key.key',
        )
    repo = {}
    baserepo = req.request('GET', mirror_url).data.decode('utf-8')
    repo[repo_name] = baserepo.split('\n')
    print(repo)
    return repo

'''
step 1: region
step 2: arch
step 3: release version
'''
def get_rhel6_repos():
    rhel6_mirrors = []
    for repo_mirror in gm.rhel6_filtered_repo_mirror:
        name, url = list(repo_mirror.items())[0]
        regions = gl.get_regions()
        for region in regions[:len(regions)-2]:
            name1, url1 = gm.replace_region(name, url, region)
            for arch in RHEL6_ARCH:
                name2, url2 = gm.replace_basearch(name1, url1, arch)
                for release in RHEL6_RELEASES:
                    name3, url3 = gm.replace_releasever(name2, url2, release)
                    rhel6_mirrors.append(call_repo_url(name3, url3))
    return rhel6_mirrors
