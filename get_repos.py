import get_links as gl
import extract_rpms as exrpms
import get_mirrors as gm

rhel6_filtered_repo_mirror = []
rhel7_filtered_repo_mirror = []
rhel8_filtered_repo_mirror = []

def get_mirror_list():
    exrpms.make_dir()
    exrpms.download_rhel6_rpms()
    exrpms.download_rhel7_rpms()
    exrpms.download_rhel8_rpms()
    gm.combine_certs()
    gm.combine_keys()
    gm.get_ca()
    global rhel6_filtered_repo_mirror
    rhel6_filtered_repo_mirror = gm.get_repo_specifics(gm.get_rhel6_repo_files())
    global rhel7_filtered_repo_mirror
    rhel7_filtered_repo_mirror = gm.get_repo_specifics(gm.get_rhel7_repo_files())
    global rhel8_filtered_repo_mirror
    rhel8_filtered_repo_mirror = gm.get_repo_specifics(gm.get_rhel8_repo_files())
    print('rhel6 repo list: ' + str(len(rhel6_filtered_repo_mirror)))
    for i in rhel6_filtered_repo_mirror:
        print(i)
    print('rhel7 repo list: ' + str(len(rhel7_filtered_repo_mirror)))
    for i in rhel7_filtered_repo_mirror:
        print(i)
    print('rhel8 repo list: ' + str(len(rhel8_filtered_repo_mirror)))
    for i in rhel8_filtered_repo_mirror:
        print(i)


'''
Next step, call mirrorlist and get repo URL
'''

def main():
    get_mirror_list()

main()