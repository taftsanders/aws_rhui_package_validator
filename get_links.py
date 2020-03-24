import os
import urllib3
import bs4


PARENT = 'http://download-node-02.eng.bos.redhat.com/brewroot/packages/rh-amazon-rhui-client/'
RHEL6 = '1.el6/noarch'
RHEL7 = '1.el7/noarch'
RHEL8 = '1.el8/noarch'
PACKAGE = ''
REGION_URL = 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html'
req = urllib3.PoolManager()

def get_latest_version():
    rpm_version = req.request('GET', PARENT)
    soup = bs4.BeautifulSoup(rpm_version.data, 'html.parser')
    latest = soup.find_all("a")[-5].text
    return latest

VERSION = get_latest_version()

def get_rhel6_rpms():
    rhel6_rpms = []
    rpm_page = req.request('GET', PARENT + VERSION + RHEL6)
    soup = bs4.BeautifulSoup(rpm_page.data, 'html.parser')
    endpoints = soup.find_all("a")[5:-5]
    for link in endpoints:
        rhel6_rpms.append(link.text)

def get_rhel7_rpms():
    rhel7_rpms = []
    rpm_page = req.request('GET', PARENT + VERSION + RHEL7)
    soup = bs4.BeautifulSoup(rpm_page.data, 'html.parser')
    endpoints = soup.find_all("a")[5:-5]
    for link in endpoints:
        rhel7_rpms.append(link.text)

def get_rhel8_rpms():
    rhel8_rpms = []
    rpm_page = req.request('GET', PARENT + VERSION + RHEL8)
    soup = bs4.BeautifulSoup(rpm_page.data, 'html.parser')
    endpoints = soup.find_all("a")[5:-5]
    for link in endpoints:
        rhel8_rpms.append(link.text)

def get_regions():
    regions = []
    region_page = req.request('GET', REGION_URL)
    soup = bs4.BeautifulSoup(region_page.data, 'html.parser')
    td = 1
    while td < len(soup.table('td')):
        regions.append(td)
        td+=4