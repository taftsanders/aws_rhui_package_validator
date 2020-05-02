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

AWS_INST_HEADER = {}
RHEL6_CERTS = '/tmp/rhui-client-rpms/rhel6/certs'
RHEL7_CERTS = '/tmp/rhui-client-rpms/rhel7/certs'
RHEL8_CERTS = '/tmp/rhui-client-rpms/rhel8/certs'

def get_instance_headers(AWS_HOST = 'ec2-3-86-214-153.compute-1.amazonaws.com',
                            AWS_USER = 'ec2-user',
                            SSH_KEY = '/home/tasander/.ssh/tasander.cer'
                            ):
    env.user = AWS_USER
    env.use_ssh_config = True
    env.key_filename = SSH_KEY
    with settings(hide('everything'), host_string=AWS_HOST):
        results = fabric_run('sudo yum repolist | grep X-RHUI')
    global AWS_INST_HEADER
    AWS_INST_HEADER['X-RHUI-ID'] = results.split()[1]
    AWS_INST_HEADER['X-RHUI-SIGNATURE'] = results.split()[3]

'''
Make the calls here to get the repodata and parse it
'''
def get_RHEL6_repomd():
    for dic in gr.get_rhel6_repos():
        name, values = list(dic.items())[0]
        req = urllib3.PoolManager(
            cert_reqs = 'CERT_REQUIRED',
            ca_certs=RHEL6_CERTS + values['sslcacert'],
            cert_file = RHEL6_CERTS + values['sslclientcert'],
            key_file = RHEL6_CERTS + values['sslclientkey'],
            )
        print(name)
        for repo in values['baseurl']:
# The RHUI AWS headers have to be added to make this call
            get_instance_headers()            
            repomd = req.request('GET',
                                repo + '/repodata/repomd.xml',
                                fields=AWS_INST_HEADER,
                                )#.data.decode('utf-8')
            print('    '+repo.split('/')[2])
            print('     |--HTTP: ' + str(repomd.status))
# Check how rich parses XML
# https://github.com/RedHatSatellite/satellite-cert-pprint

#    print(len(gr.get_rhel6_repos()))

if __name__ == "__main__":
    print(get_instance_headers())
    print(get_RHEL6_repomd())