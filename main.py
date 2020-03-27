import get_links as gl
import extract_rpms as exrpms
import get_repos as gr


def main():
    exrpms.make_dir()
    exrpms.download_rhel6_rpms()
    exrpms.download_rhel7_rpms()
    exrpms.download_rhel8_rpms()
    gr.combine_certs()
    gr.combine_keys()
    gr.get_ca()
    #rhel6_repo_files = gr.get_rhel6_repo_files()
    #rhel7_repo_files = gr.get_rhel7_repo_files()
    #rhel8_repo_files = gr.get_rhel8_repo_files()
    #rhel6_repo_mirror = gr.get_repo_specifics(rhel6_repo_files)
    #rhel7_repo_mirror = gr.get_repo_specifics(rhel7_repo_files)
    #rhel8_repo_mirror = gr.get_repo_specifics(rhel8_repo_files)
    #rhel6_filtered_repo_mirror = gr.combine_like_repos(rhel6_repo_mirror)
    #rhel7_filtered_repo_mirror = gr.combine_like_repos(rhel7_repo_mirror)
    #rhel8_filtered_repo_mirror = gr.combine_like_repos(rhel8_repo_mirror)
    rhel6_filtered_repo_mirror = gr.combine_like_repos(gr.get_repo_specifics(gr.get_rhel6_repo_files()))
    rhel7_filtered_repo_mirror = gr.combine_like_repos(gr.get_repo_specifics(gr.get_rhel7_repo_files()))
    rhel8_filtered_repo_mirror = gr.combine_like_repos(gr.get_repo_specifics(gr.get_rhel8_repo_files()))
    print(rhel6_filtered_repo_mirror)
    print(rhel7_filtered_repo_mirror)
    print(rhel8_filtered_repo_mirror)

main()