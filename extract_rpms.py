import os
import rpm
import wget
import shutil
import get_links as gl
PARENT='/tmp/rhui-client-rpms'
RHEL6_DIR='/tmp/rhui-client-rpms/rhel6/'
RHEL7_DIR='/tmp/rhui-client-rpms/rhel7/'
RHEL8_DIR='/tmp/rhui-client-rpms/rhel8/'

def make_dir():
    try:
        if os.path.exists(PARENT):
            shutil.rmtree(PARENT)
            os.mkdir(PARENT)
            os.mkdir(RHEL6_DIR)
            os.mkdir(RHEL7_DIR)
            os.mkdir(RHEL8_DIR)
        else:
            os.mkdir(PARENT)
            os.mkdir(RHEL6_DIR)
            os.mkdir(RHEL7_DIR)
            os.mkdir(RHEL8_DIR)
    except OSError:
        print("Could not create the /tmp/rhui-client-rpms directory")

def download_rhel6_rpms():
    os.chdir(RHEL6_DIR)
    #gl.get_latest_version()
    for rpm in gl.get_rhel6_rpms():
        try:
            os.mkdir(rpm)
        except FileExistsError:
            shutil.rmtree(rpm)
            os.mkdir(rpm)
        os.chdir(RHEL6_DIR + rpm)
        print(rpm)
        wget.download(gl.PARENT + gl.VERSION + gl.RHEL6 + rpm)
        extract(rpm)
        os.chdir(RHEL6_DIR)

def download_rhel7_rpms():
    os.chdir(RHEL7_DIR)
    #gl.get_latest_version()
    for rpm in gl.get_rhel7_rpms():
        try:
            os.mkdir(rpm)
        except FileExistsError:
            shutil.rmtree(rpm)
            os.mkdir(rpm)
        os.chdir(RHEL7_DIR + rpm)
        print(rpm)
        wget.download(gl.PARENT + gl.VERSION + gl.RHEL7 + rpm)
        extract(rpm)
        os.chdir(RHEL7_DIR)


def download_rhel8_rpms():
    os.chdir(RHEL8_DIR)
    #gl.get_latest_version()
    for rpm in gl.get_rhel8_rpms():
        try:
            os.mkdir(rpm)
        except FileExistsError:
            shutil.rmtree(rpm)
            os.mkdir(rpm)
        os.chdir(RHEL8_DIR + rpm)
        print(rpm)
        wget.download(gl.PARENT + gl.VERSION + gl.RHEL8 + rpm)
        extract(rpm)
        os.chdir(RHEL8_DIR)


def extract(rpm):
    os.system('rpm2cpio ' + rpm + ' | cpio -idu')
    
if __name__ == "__main__":
    make_dir()
    download_rhel6_rpms()
    download_rhel7_rpms()
    download_rhel8_rpms()
