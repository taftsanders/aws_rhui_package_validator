import get_repomd as repomd
import extract_rpms as exrpms
import get_mirrors as gm

def main():
    repomd.get_instance_headers()
    repomd.get_RHEL6_repomd()

main()