# aws_rhui_package_validator

This project is designed to use the primary.xml.gz package count to determine the repository package number and compare with all regions from:
https://access.redhat.com/articles/4720861

---
```
get_links.py - scrape for latest rpm
extract_rpms.py - download latest rpms
extract_rpms.py - extract rpms
get_links.py - scrape region list 
get_repos.py - combine all certs
get_repos.py - grep all repo names
get_repos.py - grep all mirror list urls
Needed? -- replace 'mirror' with repos 
 - would cut down on run time to sed all instances of REGION with the region name
 - wouldn't validate that mirrorlist url provides a repo url
get_repos.py - sort and combine unique
get_repos.py - make a cert chain of all certs and keys?
get_links.py - make main file to call all repos for all/unique region
```