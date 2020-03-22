import os
import urllib3
import bs4


PARENT = 'http://download-node-02.eng.bos.redhat.com/brewroot/packages/rh-amazon-rhui-client/'
VERSION = get_latest_version()
RHEL6 = '1.el6/noarch'
RHEL7 = '1.el7/noarch'
RHEL8 = '1.el8/noarch'
PACKAGE = ''
req = urllib3.PoolManager()

def get_latest_version():
    rpm_version = req.request('GET', PARENT)
    soup = bs4.BeautifulSoup(rpm_version.data)
    latest = soup.find_all("a")[-5].text
    return latest

def get_rhel6_rpms():
    rhel6_rpms = []
    rpm_page = req.request('GET', PARENT + VERSION + RHEL6)
    soup = bs4.BeautifulSoup(rpm_page.data)
    endpoints = soup.find_all("a")[5:-5]
    for link in endpoints:
        rhel6_rpms.append(link.text)

def get_rhel7_rpms():
    rhel7_rpms = []
    rpm_page = req.request('GET', PARENT + VERSION + RHEL7)
    soup = bs4.BeautifulSoup(rpm_page.data)
    endpoints = soup.find_all("a")[5:-5]
    for link in endpoints:
        rhel7_rpms.append(link.text)

def get_rhel8_rpms():
    rhel8_rpms = []
    rpm_page = req.request('GET', PARENT + VERSION + RHEL8)
    soup = bs4.BeautifulSoup(rpm_page.data)
    endpoints = soup.find_all("a")[5:-5]
    for link in endpoints:
        rhel8_rpms.append(link.text)
