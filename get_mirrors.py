import os
import glob
import configparser
from shutil import copyfile
from shutil import rmtree
import extract_rpms as exrpms

PARENT_HOME = '/tmp/rhui-client-rpms/'
RHEL6_HOME = '/tmp/rhui-client-rpms/rhel6/'
RHEL7_HOME = '/tmp/rhui-client-rpms/rhel7/'
RHEL8_HOME = '/tmp/rhui-client-rpms/rhel8/'


rhel6_filtered_repo_mirror = []
rhel7_filtered_repo_mirror = []
rhel8_filtered_repo_mirror = []

def get_rhel6_repo_files():
    exrpms.download_rhel6_rpms()
    repo_files=[]
    os.chdir(RHEL6_HOME)
    try:
        os.mkdir(RHEL6_HOME + 'certs/')
    except FileExistsError:
        rmtree(RHEL6_HOME + 'certs')
        os.mkdir(RHEL6_HOME + 'certs/')
    for file in glob.iglob('**/*.repo', recursive=True):
        repo_files.append(RHEL6_HOME + file)
    for cert in glob.iglob('**/*.crt', recursive=True):
        os.makedirs(os.path.dirname('certs/' + cert.split('/',1)[1]), exist_ok=True)
        copyfile(cert, RHEL6_HOME + 'certs/' + cert.split('/',1)[1])
    for key in glob.iglob('**/*.key', recursive=True):
        os.makedirs(os.path.dirname('certs/' + key.split('/',1)[1]), exist_ok=True)
        copyfile(key, RHEL6_HOME + 'certs/' + key.split('/',1)[1])
    return repo_files

def get_rhel7_repo_files():
    exrpms.download_rhel7_rpms()
    repo_files=[]
    os.chdir(RHEL7_HOME)
    try:
        os.mkdir(RHEL7_HOME + 'certs/')
    except FileExistsError:
        rmtree(RHEL7_HOME + 'certs')
        os.mkdir(RHEL7_HOME + 'certs/')
    for file in glob.iglob('**/*.repo', recursive=True):
        repo_files.append(RHEL7_HOME + file)
    for cert in glob.iglob('**/*.crt', recursive=True):
        os.makedirs(os.path.dirname('certs/' + cert.split('/',1)[1]), exist_ok=True)
        copyfile(cert, RHEL7_HOME + 'certs/' + cert.split('/',1)[1])
    for key in glob.iglob('**/*.key', recursive=True):
        os.makedirs(os.path.dirname('certs/' + key.split('/',1)[1]), exist_ok=True)
        copyfile(key, RHEL7_HOME + 'certs/' + key.split('/',1)[1])
    return repo_files

def get_rhel8_repo_files():
    exrpms.download_rhel8_rpms()
    repo_files=[]
    os.chdir(RHEL8_HOME)
    try:
        os.mkdir(RHEL8_HOME + 'certs/')
    except FileExistsError:
        rmtree(RHEL8_HOME + 'certs')
        os.mkdir(RHEL8_HOME + 'certs/')
    for file in glob.iglob('**/*.repo', recursive=True):
        repo_files.append(RHEL8_HOME + file)
    for cert in glob.iglob('**/*.crt', recursive=True):
        os.makedirs(os.path.dirname('certs/' + cert.split('/',1)[1]), exist_ok=True)
        copyfile(cert, RHEL8_HOME + 'certs/' + cert.split('/',1)[1])
    for key in glob.iglob('**/*.key', recursive=True):
        os.makedirs(os.path.dirname('certs/' + key.split('/',1)[1]), exist_ok=True)
        copyfile(key, RHEL8_HOME + 'certs/' + key.split('/',1)[1])
    return repo_files

#Combining certs doesn't work
#Combining keys doesn't work
'''
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
'''
'''
Test repo_files Output:
['rh-amazon-rhui-client-rhs30-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui-rhs30.repo', 'rh-amazon-rhui-client-rhs30-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui-client-config-rhs30.repo', 'rh-amazon-rhui-client-jbeap72-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui-jbeap-7.2.repo', 'rh-amazon-rhui-client-jbeap72-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui-client-config-jbeap-7.2.repo', 'rh-amazon-rhui-client-jbeap71-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui-jbeap-7.1.repo', 'rh-amazon-rhui-client-jbeap71-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui-client-config-jbeap-7.1.repo', 'rh-amazon-rhui-client-jbeap70-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui-jbeap-7.0.repo', 'rh-amazon-rhui-client-jbeap70-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui-client-config-jbeap-7.0.repo', 'rh-amazon-rhui-client-jbeap7-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui-jbeap7.repo', 'rh-amazon-rhui-client-jbeap7-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui-client-config-jbeap7.repo', 'rh-amazon-rhui-client-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui.repo', 'rh-amazon-rhui-client-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui-client-config.repo', 'rh-amazon-rhui-client-3.0.26-1.el6.noarch.rpm/etc/yum.repos.d/redhat-rhui-beta.repo']
'''
def get_repo_specifics(repo_files):
    repo_list = []
    uniq_list = []
    for file in repo_files:
        config = configparser.ConfigParser()
        config.read(file)
        for section in config.sections():
            if section not in uniq_list:
                uniq_list.append(section)
                name = {}
                name[section]={}
                name[section]['mirrorlist'] = config[section]['mirrorlist']
                name[section]['sslcacert'] = config[section]['sslcacert']
                name[section]['sslclientcert'] = config[section]['sslclientcert']
                name[section]['sslclientkey'] = config[section]['sslclientkey']
                repo_list.append(name)
            else:
                pass
    return repo_list

def get_mirror_list():
    exrpms.make_dir()
    global rhel6_filtered_repo_mirror
    rhel6_filtered_repo_mirror = get_repo_specifics(get_rhel6_repo_files())
    global rhel7_filtered_repo_mirror
    rhel7_filtered_repo_mirror = get_repo_specifics(get_rhel7_repo_files())
    global rhel8_filtered_repo_mirror
    rhel8_filtered_repo_mirror = get_repo_specifics(get_rhel8_repo_files())

if __name__ == "__main__":
    print('get_rhel6_repo_files: ')
    print(get_rhel6_repo_files())
    print('get_rhel7_repo_files: ')
    print(get_rhel7_repo_files())
    print('get_rhel8_repo_files: ')
    print(get_rhel8_repo_files())
    get_mirror_list()
    print('rhel6_filtered_repo_mirror: ' + str(len(rhel6_filtered_repo_mirror)))
    print(rhel6_filtered_repo_mirror)
    print('rhel7_filtered_repo_mirror: ' + str(len(rhel7_filtered_repo_mirror)))
    print(rhel7_filtered_repo_mirror)
    print('rhel8_filtered_repo_mirror: ' + str(len(rhel8_filtered_repo_mirror)))
    print(rhel8_filtered_repo_mirror)

