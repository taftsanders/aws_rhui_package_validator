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

'''
step 1: region
step 2: repo
step 3: arch
step 4: release version
'''
def get_rhel6_repos():
    rhel6_mirrors = []
    regions = gl.get_regions()
    for region in regions[:len(regions)-2]:
        req = urllib3.PoolManager(
            cert_reqs = 'CERT_REQUIRED',
            ca_certs='/tmp/rhui-client-rpms/rhui-ca.crt',
            cert_file = '/tmp/rhui-client-rpms/master-content-cert.crt',
            key_file = '/tmp/rhui-client-rpms/master-content-key.key',
            )
        for repo_mirror in gm.rhel6_filtered_repo_mirror:
            name, url = list(repo_mirror.items())[0]           
            name1, url1 = gm.replace_region(name, url, region)
            for arch in RHEL6_ARCH:
                name2, url2 = gm.replace_basearch(name1, url1, arch)
                for release in RHEL6_RELEASES:
                    name3, url3 = gm.replace_releasever(name2, url2, release)
                    repo = {}
                    baserepo = req.request('GET', url3).data.decode('utf-8')
                    repo[name3] = baserepo.split('\n')
                    print(repo)
                    rhel6_mirrors.append(repo)
    return rhel6_mirrors
