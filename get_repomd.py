import os
import get_repos as gr
import get_mirrors as gm

'''
Make the calls here to get the repodata and parse it
'''
def devariabled_values():
    gm.get_mirror_list()
    print(len(gr.get_rhel6_repos()))

