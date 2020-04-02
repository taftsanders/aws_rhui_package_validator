import os
import get_repos as gr
import get_mirrors as gm

'''
Make the calls here to get the repodata and parse it
'''
def devariabled_values():
    gm.get_mirror_list()
    all_repo_mirrors = gm.combine_lists(gm.rhel6_filtered_repo_mirror,
                                        gm.rhel7_filtered_repo_mirror, 
                                        gm.rhel8_filtered_repo_mirror)
    #variable1 = gm.replace_variables(all_repo_mirrors)
    #print(variable1)
    #print(len(variable1))