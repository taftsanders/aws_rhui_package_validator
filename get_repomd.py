import os
import get_repos as gr
import get_mirrors as gm
import urllib3
import configparser
from fabric.api import env
from fabric.operations import run as fabric_run
from fabric.context_managers import settings, hide 
import xmltodict as x2d
import gzip
import warnings
warnings.simplefilter('ignore', urllib3.exceptions.SecurityWarning)

AWS_INST_HEADER = {}
RHEL6_CERTS = '/tmp/rhui-client-rpms/rhel6/certs'
RHEL7_CERTS = '/tmp/rhui-client-rpms/rhel7/certs'
RHEL8_CERTS = '/tmp/rhui-client-rpms/rhel8/certs'

def get_aws_instance_headers(AWS_HOST=None, AWS_USER=None, SSH_KEY=None):
    env.user = AWS_USER
    env.use_ssh_config = True
    env.key_filename = SSH_KEY
    with settings(hide('everything'), host_string=AWS_HOST):
        results = fabric_run('sudo yum repolist | grep X-RHUI')
    global AWS_INST_HEADER
    #print(results)
    AWS_INST_HEADER['X-RHUI-ID'] = results.split()[1]
    #print(AWS_INST_HEADER['X-RHUI-ID'])
    AWS_INST_HEADER['X-RHUI-SIGNATURE'] = results.split()[3]
    #print(AWS_INST_HEADER['X-RHUI-SIGNATURE'])

'''
Make the calls here to get the repodata and parse it
'''
def get_RHEL6_repomd(sslcacert=None, sslclientcert=None, sslclientkey=None, baseurl=None):
        for dic in gr.get_rhel6_repos():
            name, values = list(dic.items())[0]
            if sslcacert==None and sslclientcert==None and sslclientkey==None:
                req = urllib3.PoolManager(
                    cert_reqs = 'CERT_REQUIRED',
                    ca_certs = RHEL6_CERTS + values['sslcacert'],
                    cert_file = RHEL6_CERTS + values['sslclientcert'],
                    key_file = RHEL6_CERTS + values['sslclientkey'],
                    )
                #print('ca_file:' + RHEL6_CERTS + values['sslcacert']) #DEBUG
                #print('cert_file: ' + RHEL6_CERTS + values['sslclientcert']) #DEBUG
                #print('key_file: ' + RHEL6_CERTS + values['sslclientkey']) #DEBUG
            elif sslcacert!=None and sslclientcert!=None and sslclientcert!=None:
                req = urllib3.PoolManager(
                    cert_reqs = 'CERT_REQUIRED',
                    ca_certs = sslcacert,
                    cert_file = sslclientcert,
                    key_file = sslclientkey,
                    )
                #print('ca_file: ' + sslcacert) #DEBUG
                #print('cert_file: ' + sslclientcert) #DEBUG
                #print('key_file: ' + sslclientkey) #DEBUG
            print(name)
            if baseurl == None:
                for repo in values['baseurl']:
    # The RHUI AWS headers have to be added here to make this call
                    get_aws_instance_headers()
                    #print(repo + '/repodata/repomd.xml') #DEBUG
                    repomd = req.request('GET',
                            repo + '/repodata/repomd.xml', headers=AWS_INST_HEADER)#.data.decode('utf-8')
                    print('    '+repo.split('/')[2])
                    if repomd.status != 200:
                        print('     |--HTTP: ' + str(repomd.status))
                    else:
                        primary_href = x2d.parse(repomd.data.decode('utf-8'))['repomd']['data'][2]['location']['@href']
                        #print(primary_href) #DEBUG
                        primary = req.request('GET',
                                        repo + '/' + primary_href,
                                        headers=AWS_INST_HEADER,
                                        )
                        package_count = str(urllib3.response.GzipDecoder().decompress(primary.data)).split( )[3][10:][:-1]
                        print(package_count)
            elif baseurl != None:
                get_aws_instance_headers()
                repomd = req.request('GET',
                            baseurl + '/repodata/repomd.xml', headers=AWS_INST_HEADER)#.data.decode('utf-8')
                print('    '+baseurl.split('/')[2])
                if repomd.status != 200:
                    print('     |--HTTP: ' + str(repomd.status))
                else:
                    primary_href = x2d.parse(repomd.data.decode('utf-8'))['repomd']['data'][2]['location']['@href']
                    #print(primary_href) #DEBUG
                    primary = req.request('GET',
                                    baseurl + '/' + primary_href,
                                    headers=AWS_INST_HEADER,
                                    )
                    package_count = str(urllib3.response.GzipDecoder().decompress(primary.data)).split( )[3][10:][:-1]
                    print(package_count)
#    print(Total number of repos for RHEL 6: str(len(gr.get_rhel6_repos()))) #DEBUG

if __name__ == "__main__":
    print(get_aws_instance_headers())
    print(get_RHEL6_repomd())