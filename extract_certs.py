import os
import rpm
import wget
import get_links as gl
PARENT='/tmp/rhui-client-rpms'
RHEL6_DIR='/tmp/rhui-client-rpms/rhel6/'
RHEL7_DIR='/tmp/rhui-client-rpms/rhel7/'
RHEL8_DIR='/tmp/rhui-client-rpms/rhel8/'

try:
    if os.mkdir(PARENT):
        os.mkdir(RHEL6_DIR)
        os.mkdir(RHEL7_DIR)
        os.mkdir(RHEL8_DIR)
except OSError:
    print("Could not create the /tmp/rhui-client-rpms directory")
    exit

def download_rhel6_rpms():
    os.chdir(RHEL6_DIR)
    #gl.get_latest_version()
    for rpm in gl.get_rhel6_rpms():
        os.mkdir(rpm)
        os.chdir(PARENT + rpms)
        wget.download(rpm)
        extract(rpm)

def download_rhel7_rpms():
    os.chdir(RHEL7_DIR)
    #gl.get_latest_version()
    for rpm in gl.get_rhel7_rpms():
        os.mkdir(rpm)
        os.chdir(PARENT + rpm)
        wget.download(rpm)
        extract(rpm)

def download_rhel8_rpms():
    os.chdir(RHEL8_DIR)
    #gl.get_latest_version()
    for rpm in gl.get_rhel8_rpms():
        os.mkdir(rpm)
        os.chdir(PARENT + rpm)
        wget.download(rpm)
        extract(rpm)

def extract():
    os.system('rpm2cpio ' + rpm + ' | cpio -id')
    
