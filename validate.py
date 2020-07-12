import get_repomd as repomd
import extract_rpms as exrpms
import get_mirrors as gm
import get_links as gl
import textwrap

def main():
    import argparse
    parser = argparse.ArgumentParser(prog='validate',
                                    usage='%(prog)s <ENVIRONMENT> [options]',
                                    description='Validate the contents of a repository in any environment')
    parser.add_argument('--debug',
                    action='store_true',
                    help='enable debugging messages')
    subparsers = parser.add_subparsers(title='ENVIRONMENTS',
                                        dest='command')

    #AWS Parser Options
    aws_parser = subparsers.add_parser('aws',
                                        help='Amazon Web Services')
    aws_parser.add_argument('--awshost',
                            action='store',
                            type=str,
                            nargs=1,
                            required=True,
                            help='aws system in which to extract AWS ID & Signature from')
    aws_parser.add_argument('--user',
                            action='store',
                            type=str,
                            nargs=1,
                            required=True,
                            help='the user to ssh into the host with')
    aws_parser.add_argument('--sshkey',
                            action='store',
                            type=str,
                            nargs=1,
                            required=True,
                            help='the ssh public key to ssh into the host')
    aws_parser.add_argument('--version',
                            action='store',
                            type=int,
                            nargs=1,
                            help='Major version in which to query for')
    aws_parser.add_argument('--region',
                            action='store',
                            type=str,
                            nargs=1,
                            help='AWS region from the table on: '+ gl.REGION_URL)
    aws_parser.add_argument('--repo',
                            action='store',
                            type=str,
                            nargs=1,
                            help='Include the repository labels you want to query')
    aws_parser.add_argument('--arch',
                            action='store',
                            type=str,
                            nargs=1,
                            help='Include the arch for the repository')
    aws_parser.add_argument('--baseurl',
                            action='store',
                            type=str,
                            nargs=1,
                            help='the baseurl for the repository to query')
    aws_parser.add_argument('--mirrorlist',
                            action='store',
                            type=str,
                            nargs=1,
                            help='the mirrorlist for the repository to query')
    aws_parser.add_argument('--releasever',
                            action='store',
                            type=str,
                            nargs=1,
                            help='the release version of the repository to query')
    aws_parser.add_argument('--sslcacert',
                            action='store',
                            type=str,
                            nargs=1,
                            help='the CA cert to use for the request')
    aws_parser.add_argument('--sslclientcert',
                            action='store',
                            type=str,
                            nargs=1,
                            help='the entitlement cert to use for the request')
    aws_parser.add_argument('--sslclientkey',
                            action='store',
                            type=str,
                            nargs=1,
                            help='the entitlement key to use for the request')
    aws_parser.add_argument('--rpm',
                            action='store',
                            type=str,
                            nargs=1,
                            help='the RPM to query for')


    #Azure Parser Options
    azure_parser = subparsers.add_parser('azure',
                                            help='Microsoft Azure (features coming soon!)')
    azure_parser.add_argument('--azurehost',
                                action='store',
                                type=str,
                                nargs=1,
                                help='azure system in which to extract information')
    
    # CDN Parser Options
    cdn_parser = subparsers.add_parser('cdn',
                                        help='Red Hat CDN (features coming soon!)')
    cdn_parser.add_argument('--cdn-cert',
                            action='store',
                            type=str,
                            nargs=1,
                            help='a entitlement certificate for the repo you wish to query')
    cdn_parser.add_argument('--cdn-key',
                            action='store',
                            type=str,
                            nargs=1,
                            help='a entitlement key for the repo you wish to query')
    args = parser.parse_args()

    if args.awshost != None:
        repomd.get_aws_instance_headers(args.awshost[0], args.user[0], args.sshkey[0])
        repomd.get_RHEL6_repomd()

main()