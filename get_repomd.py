import os
import get_repos as gr
import get_mirrors as gm
import urllib3
import configparser
from fabric.api import env
from fabric.operations import run as fabric_run
from fabric.context_managers import settings, hide 
import warnings
warnings.simplefilter('ignore', urllib3.exceptions.SecurityWarning)

X_RHUI_ID = ''
X_RHUI_SIGNATURE = ''

def get_instance_headers(AWS_HOST = 'ec2-3-86-214-153.compute-1.amazonaws.com',
                            AWS_USER = 'ec2-user',
                            SSH_KEY = '/home/tasander/.ssh/tasander.cer'
                            ):
    env.user = AWS_USER
    env.use_ssh_config = True
    env.key_filename = SSH_KEY
    with settings(hide('everything'), host_string=AWS_HOST):
        results = fabric_run('sudo yum repolist | grep X-RHUI')
    global X_RHUI_ID
    X_RHUI_ID = results.split()[1]
    global X_RHUI_SIGNATURE
    X_RHUI_SIGNATURE = results.split()[3]

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

