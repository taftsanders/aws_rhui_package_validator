import os
import glob
import configparser

config = configparser.ConfigParser()

def get_rhel6_repo_files():
    repo_files=[]
    os.chdir('/tmp/rhui-client-rpms/rhel6/')
    for file in glob.iglob('**/*.repo', recursive=True):
        repo_files.append(file)
    return repo_files

def get_rhel7_repo_files():
    repo_files=[]
    os.chdir('/tmp/rhui-client-rpms/rhel7/')
    for file in glob.iglob('**/*.repo', recursive=True):
        repo_files.append(file)
    return repo_files

def get_rhel8_repo_files():
    repo_files=[]
    os.chdir('/tmp/rhui-client-rpms/rhel8/')
    for file in glob.iglob('**/*.repo', recursive=True):
        repo_files.append(file)
    return repo_files

def combine_certs():
    os.chdir('/tmp/rhui-client-rpms/')
    for file in glob.iglob('*/*/etc/pki/rhui/product/*.crt', recursive=True): 
         with open(file, 'r') as cert: 
            with open('master-content-cert.crt', 'a') as master:
                master.write(cert.read())

def combine_keys():
    os.chdir('/tmp/rhui-client-rpms/')
    for file in glob.iglob('*/*/etc/pki/rhui/*.key', recursive=True): 
         with open(file, 'r') as key: 
            with open('master-content-key.key', 'a') as master:
                master.write(key.read())

# What if the CA is bad in cert[0], future code should include comparison check for these certs
def get_ca():
    os.chdir('/tmp/rhui-client-rpms/')
    ca_files=[]
    for ca in glob.iglob('*/*/etc/pki/rhui/cdn.redhat.com-chain.crt', recursive=True):
        ca_files.append(ca)
    with open(ca_files[0], 'r') as ca:
        with open('rhui-ca.crt', 'w') as master:
            master.write(ca.read())

# Create a nested dict of all repos from all repo files passed in
# {file:{
#       repo name:{
#               mirrorlist:
#               sslcacert:
#               sslclientcert:
#               sslclientkey:
# }}}
def get_repo_specifics(repo_files):
#    repo_list = {}
#    for file in repo_files:
#        config.read(file)
#        repo_list[file]={}
#        for i in config.sections():
#            repo_list[file][i]={}
#            repo_list[file][i]['mirrorlist'] = config[i]['mirrorlist'] 
#            repo_list[file][i]['sslcacert'] = config[i]['sslcacert']   # removed because all certs are combined
#            repo_list[file][i]['sslclientcert'] = config[i]['sslclientcert'] # removed because all certs are combined
#            repo_list[file][i]['sslclientkey'] = config[i]['sslclientkey'] # removed because all certs are combined
#    return repo_list
    repo_list = []
    for file in repo_files: 
        config.read(file) 
        for mirror in config.sections(): 
            mirror_dict = {} 
            mirror_dict[mirror] = config[mirror]['mirrorlist'] 
            repo_list.append(mirror_dict)
    new_list = []
    for repo in repo_list:
        if repo not in new_list:
            new_list.append(repo)

def combine_like_repos(repo_list):
    repos = []
    for file in repo_list.keys():
        for name in repo_list[file].keys():
            repos.append(name)
    repos= set(repos)

