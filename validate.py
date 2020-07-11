import get_repomd as repomd
import extract_rpms as exrpms
import get_mirrors as gm
import get_links as gl
import textwrap

def main():
    repomd.get_RHEL6_repomd()

    '''
    Options for new features to come!
    import argparse
    parser = argparse.ArgumentParser(prog='validate',
                                    usage='%(prog)s [options] path',
                                    description='Validate the contents of a repository')

    parser.add_argument('--version',
                        action='store',
                        type=int,
                        nargs=1,
                        help='Major version in which to query for')
    parser.add_argument('-R',
                        '--region',
                        action='store',
                        type=str,
                        nargs='*',
                        help='AWS region from the table on: '+ gl.REGION_URL)
    parser.add_argument('-r',
                        '--repo',
                        action='store',
                        type=str,
                        nargs='*',
                        help='Include the repository labels you want to query')
    parser.add_argument('--arch',
                         action='store',
                         type=str,
                         nargs='*',
                         help='Include the arch for the repository')
    parser.add_argument('--awshost',
                        action='store',
                        type=str,
                        nargs=1,
                        help='aws system in which to extract AWS ID & Signature from')
    parser.add_argument('--user',
                        action='store',
                        type=str,
                        nargs=1,
                        help='the user to ssh into the host with')
    parser.add_argument('--sshkey',
                        action='store',
                        type=str,
                        nargs=1,
                        help='the ssh public key to ssh into the host')
    parser.add_argument('--baseurl',
                        action='store',
                        type=str,
                        nargs='*',
                        help='the baseurl for the repository to query')
    parser.add_argument('--mirrorlist',
                        action='store',
                        type=str,
                        nargs='*',
                        help='the mirrorlist for the repository to query')
    parser.add_argument('--releasever',
                        action='store',
                        type=str,
                        nargs='*',
                        help='the release version of the repository to query')
    parser.add_argument('--sslcacert',
                        action='store',
                        type=str,
                        nargs=1,
                        help='the CA cert to use for the request')
    parser.add_argument('--sslclientcert',
                        action='store',
                        type=str,
                        nargs='*',
                        help='the entitlement cert to use for the request')
    parser.add_argument('--sslclientkey',
                        action='store',
                        type=str,
                        nargs='*',
                        help='the entitlement key to use for the request')
    parser.add_argument('--rpm',
                        action='store',
                        type=str,
                        nargs='*',
                        help='the RPM to query for')
    parser.add_argument('--debug',
                        action='store_true',
                        help='enable debugging messages')
    parser.add_argument('--cloud',
                        choices=['aws', 'azure'],
                        help='the cloud environment you want to query')
    parser.add_argument('--cdn',
                        action='store_true',
                        help='set query server as cdn.redhat.com')
    parser.add_argument('--cdn-cert',
                        action='store',
                        type=str,
                        nargs=1,
                        help='a entitlement certificate for the repo'
                        'you wish to query')
    parser.add_argument('--cdn-key',
                        action='store',
                        type=str,
                        nargs=1,
                        help='a entitlement key for the repo you wish to query')
    args = parser.parse_args()
    '''

main()