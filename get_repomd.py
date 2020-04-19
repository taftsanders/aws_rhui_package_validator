import os
import get_repos as gr
import get_mirrors as gm
import urllib3
import warnings
warnings.simplefilter('ignore', urllib3.exceptions.SecurityWarning)


'''
Make the calls here to get the repodata and parse it
'''
def get_RHEL6_repomd():
    gm.get_mirror_list()
    for dic in gr.get_rhel6_repos():
        name, url = list(dic.items())[0]
        req = urllib3.PoolManager(
            cert_reqs = 'CERT_REQUIRED',
            ca_certs='/tmp/rhui-client-rpms/rhui-ca.crt',
            cert_file = '/tmp/rhui-client-rpms/master-content-cert.crt',
            key_file = '/tmp/rhui-client-rpms/master-content-key.key',
            )
        for repo in url:
# The RHUI AWS headers have to be added to make this call            
            req.request('GET', repo).data.decode('utf-8')
#    print(len(gr.get_rhel6_repos()))

