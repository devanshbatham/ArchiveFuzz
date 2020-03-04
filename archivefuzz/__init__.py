from collections import Counter
import re
import os

def email_finder(domain, r):
    """
        Finding the emails from web.archive.org server
        Input:
            domain: str: target domain name
            r: Web archive response
        Output: All data that has email syntax
    """
    first_sub = ' \u001b[32m|\u001b[0m'
    second_sub = '\u001b[32m|--\u001b[0m'
    print("\n\u001b[32m  [~] Email enumeration started\u001b[0m")
    print(" \u001b[32m  |")
    
    # I was/am actually dumb , I didn't think of image names like "name@2x.jpg" , this will also be considered as an email as per my regex
    # so I blacklisted some extensions , and removed them from the raw_data , so if you get any falsepositives , add them to the below re.sub funtion
    # below line is for removing false positives 
    
    r = re.sub('(-p-|mp4|webm|JPG|pdf|html|jpg|jpeg|png|gif|bmp|svg|1x|2x|3x|4x|5x|6x|7x|9x|10x|11x|12x|13x|14x|15x)', '', r) 
    any_email_pattern = "([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]{2,7})" # pattern for matching  email 
    # Filter duplicate elements
    any_emails = set(re.findall(any_email_pattern, r)) # list of all the emails 
    print("   " + second_sub + "[+] Total unique emails found        : " + str(len(any_emails))) # printing no of unique subdomains
    print("   " + second_sub + "[+] Email scan finished ")
    return list(any_emails)


def ip_finder(domain, data):
    """
        Finding the IP Addresses web.archive.org server
        Input:
            domain: str: target domain name
            r: Web archive response
        Output: All data that has IPv4 syntax
    """

    # for interactive output 
    print("\n\u001b[32m  [~] IPv4 scan started")
    print("\u001b[32m   |")
    # interactive output
    first_sub = '\u001b[32m|\u001b[0m'
    second_sub = '\u001b[32m|--\u001b[0m' 
    
    # finding IPv4 addresses 
    ip_pattern = "(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)"
    ip_addresses = re.findall(ip_pattern, data)
    if ip_addresses:
        ip_addresses = list(set([".".join(octet) for octet in addresses]))

    print("   " + second_sub + "[+] Total unique IPs found           : " + str(len(ip_addresses)))
    print("   " + second_sub + "[+] IP scan finished ")
    
    return ip_addresses


def subdomain_finder(domain, r):
    """
        Finding subdomains from web-archive
        Input:
            domain: str: target domain name
            r: Web archive response
        Output: All data that has subdomain syntax
    """
    print("\u001b[32m  [~] Subdomain scan started")
    print("\u001b[32m   |")

    # interactive output
    first_sub = '\u001b[32m|\u001b[0m'
    second_sub = '\u001b[32m|--\u001b[0m' 

    # finding subdomains
    subdomain_pattern = '[0-9a-z]+\.' + domain #matching subdomains 
    # filter duplicate elemments
    subdomains = set(re.findall(subdomain_pattern , r))
    print("   " + second_sub + "[+] Total unique subdomains found    : " + str(len(subdomains))) # printing no of unique subdomains
    print("   " + second_sub + "[+] Subdomain scan finished ")
    return list(subdomains)


def token_finder(domain, data):
    from archivefuzz import token_utils
    """
        Input:
            domain: str: target domain name
            r: Web archive response
        Output: All data that has valid token syntax
    """
    first_sub = ' \u001b[32m|\u001b[0m'
    second_sub = '\u001b[32m|--\u001b[0m'
    print("\n\u001b[32m  [~] Secret Keys enumeration started\u001b[0m")
    print(" \u001b[32m  |")

    # for amazon secrets : 
    token_utils.amazon_secrets(data, domain)
    #for facebook Access token   
    token_utils.facebook_access(data, domain) 
    # for facebook oath tokens 
    token_utils.facebook_oath(data, domain)
    #facebook_secrets(data , domain)
    # for google api key 
    token_utils.google_api(data, domain)