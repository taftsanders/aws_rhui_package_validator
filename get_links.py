import os
import urllib3
import bs4


PARENT = 'http://download-node-02.eng.bos.redhat.com/brewroot/packages/rh-amazon-rhui-client/'
RHEL6 = '1.el6/noarch/'
RHEL7 = '1.el7/noarch/'
RHEL8 = '1.el8/noarch/'
PACKAGE = ''
REGION_URL = 'https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html'
req = urllib3.PoolManager()

def get_latest_version():
    rpm_version = req.request('GET', PARENT)
    soup = bs4.BeautifulSoup(rpm_version.data, 'html.parser')
    latest = soup.find_all("a")[-5].text
    print('Getting latest rpm version: ')
    return latest

VERSION = get_latest_version()

def get_rhel6_rpms():
    rhel6_rpms = []
    rpm_page = req.request('GET', PARENT + VERSION + RHEL6)
    soup = bs4.BeautifulSoup(rpm_page.data, 'html.parser')
    endpoints = soup.find_all("a")[5:-5]
    for link in endpoints:
        rhel6_rpms.append(link.text)
    print('RHEL6 RPMs to download: ')
    for rpm in rhel6_rpms:
        print(rpm)
    return rhel6_rpms

def get_rhel7_rpms():
    rhel7_rpms = []
    rpm_page = req.request('GET', PARENT + VERSION + RHEL7)
    soup = bs4.BeautifulSoup(rpm_page.data, 'html.parser')
    endpoints = soup.find_all("a")[5:-5]
    for link in endpoints:
        rhel7_rpms.append(link.text)
    print('RHEL7 RPMs to download: ')
    for rpm in rhel7_rpms:
        print(rpm)
    return rhel7_rpms

def get_rhel8_rpms():
    rhel8_rpms = []
    rpm_page = req.request('GET', PARENT + VERSION + RHEL8)
    soup = bs4.BeautifulSoup(rpm_page.data, 'html.parser')
    endpoints = soup.find_all("a")[5:-5]
    for link in endpoints:
        rhel8_rpms.append(link.text)
    print('RHEL8 RPMs to download: ')
    for rpm in rhel8_rpms:
        print(rpm)
    return rhel8_rpms

def get_regions():
    regions = []
    region_page = req.request('GET', REGION_URL)
    soup = bs4.BeautifulSoup(region_page.data, 'html.parser')
    td = 1
    while td < len(soup.table('td')):
        regions.append(soup.table('td')[td].text)
        td+=4
    return regions

'''
Need to find a place to scrape archs and release versions
Hard coding for now
'''

if __name__ == "__main__":
    print(get_latest_version())
    print(get_rhel6_rpms())
    print(get_rhel7_rpms())
    print(get_rhel8_rpms())
    print(get_regions())