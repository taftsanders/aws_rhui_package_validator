import os
import glob
import configparser
import extract_rpms as exrpms

rhel6_filtered_repo_mirror = []
rhel7_filtered_repo_mirror = []
rhel8_filtered_repo_mirror = []

def get_rhel6_repo_files():
    exrpms.download_rhel6_rpms()
    repo_files=[]
    os.chdir('/tmp/rhui-client-rpms/rhel6/')
    for file in glob.iglob('**/*.repo', recursive=True):
        repo_files.append(file)
    return repo_files

def get_rhel7_repo_files():
    exrpms.download_rhel7_rpms()
    repo_files=[]
    os.chdir('/tmp/rhui-client-rpms/rhel7/')
    for file in glob.iglob('**/*.repo', recursive=True):
        repo_files.append(file)
    return repo_files

def get_rhel8_repo_files():
    exrpms.download_rhel8_rpms()
    repo_files=[]
    os.chdir('/tmp/rhui-client-rpms/rhel8/')
    for file in glob.iglob('**/*.repo', recursive=True):
        repo_files.append(file)
    return repo_files

def combine_certs(dir):
    os.chdir('/tmp/rhui-client-rpms/' + dir)
    for file in glob.iglob('*/etc/pki/rhui/product/*.crt', recursive=True): 
         with open(file, 'r') as cert: 
            with open('/tmp/rhui-client-rpms/' + dir + '/master-content-cert.crt', 'a+') as master:
                master.write(cert.read())

def combine_keys(dir):
    os.chdir('/tmp/rhui-client-rpms/' + dir)
    for file in glob.iglob('*/etc/pki/rhui/*.key', recursive=True): 
         with open(file, 'r') as key: 
            with open('/tmp/rhui-client-rpms/' + dir + '/master-content-key.key', 'a+') as master:
                master.write(key.read())

# What if the CA is bad in cert[0], future code should include comparison check for these certs
def get_ca():
    os.chdir('/tmp/rhui-client-rpms/')
    ca_files=[]
    for ca in glob.iglob('*/*/etc/pki/rhui/cdn.redhat.com-chain.crt', recursive=True):
        ca_files.append(ca)
    with open(ca_files[0], 'r') as ca:
        with open('rhui-ca.crt', 'w+') as master:
            master.write(ca.read())

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
        config = configparser.ConfigParser()
        config.read(file) 
        for mirror in config.sections(): 
            mirror_dict = {} 
            mirror_dict[mirror] = config[mirror]['mirrorlist'] 
            repo_list.append(mirror_dict)
    new_list = []
    for repo in repo_list:
        if repo not in new_list:
            new_list.append(repo)
    return new_list

def get_mirror_list():
    exrpms.make_dir()
    global rhel6_filtered_repo_mirror
    rhel6_filtered_repo_mirror = get_repo_specifics(get_rhel6_repo_files())
    global rhel7_filtered_repo_mirror
    rhel7_filtered_repo_mirror = get_repo_specifics(get_rhel7_repo_files())
    global rhel8_filtered_repo_mirror
    rhel8_filtered_repo_mirror = get_repo_specifics(get_rhel8_repo_files())
    combine_certs('rhel6')
    combine_certs('rhel7')
    combine_certs('rhel8')
    combine_keys('rhel6')
    combine_keys('rhel7')
    combine_keys('rhel8')
    get_ca()
#DEBUGGING
#    print('rhel6 repo list: ' + str(len(rhel6_filtered_repo_mirror)))
#    for i in rhel6_filtered_repo_mirror:
#        print(i)
#    print('rhel7 repo list: ' + str(len(rhel7_filtered_repo_mirror)))
#   for i in rhel7_filtered_repo_mirror:
#        print(i)
#    print('rhel8 repo list: ' + str(len(rhel8_filtered_repo_mirror)))
#    for i in rhel8_filtered_repo_mirror:
#        print(i)

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
