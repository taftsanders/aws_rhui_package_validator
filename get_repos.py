import get_links as gl
import get_mirrors as gm

REGIONS = gl.get_regions()
RHEL6_RELEASES = ['6.10', '6Server']
RHEL6_ARCH = ['i386', 'x86_64']
RHEL7_RELEASES = ['7.3', '7.4', '7.5', '7.6', '7.7', '7.8']
RHEL7_ARCH = ['x86_64']
RHEL8_RELEASES = ['8']
RHEL8_ARCH = ['aarch64', 'ppc64le', 's390x', 'x86_64']