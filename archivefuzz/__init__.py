from collections import Counter
import re
import os
import errno

def email_enumerator(url, domain, r):
    """
        Finding the emails from web.archive.org server
        Input:
            url: str. This is web.archive.org URL we are using to find info about target
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
    any_emails = re.findall(any_email_pattern, r) # list of all the emails 
    cnt = Counter(any_emails) # removing duplicate emails
    print("   " + second_sub + "[+] Total unique emails found        : " + str(len(cnt))) # printing no of unique subdomains

    filename = domain + "-output/" + domain + "-emails.txt" #defining the filename
    if len(cnt) > 0: # if no of emails are not zero
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # a check to protect againsts the Racecondition issues
                if exc.errno != errno.EEXIST:
                    raise
        # if the file already exists , empty the file, this happens when you run the scan against same target multiple times
        with open(filename, 'w') as empty:
            empty.write('')

        # writing the subdomains in file
        
        for i in cnt.keys():
            with open(filename, "a") as f:
                f.write(i + "\n") # writing all the emails in a file 
        print("   " + second_sub + "[+] Emails saved in                  : {} ".format(filename))

    print("   " + second_sub + "[+] Email scan finished ")


def ip_finder(url, domain, data):
    """
        Finding the IP Addresses web.archive.org server
        Input:
            url: str. This is web.archive.org URL we are using to find info about target
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
    ip_addresses = re.findall(ip_pattern , data)
    final_ips = []

    for i in range(len(ip_addresses)):
        final_ips.append('.'.join(list(ip_addresses[i])))    
    cnt = Counter(ip_addresses)
    print("   " + second_sub + "[+] Total unique IPs found           : " + str(len(cnt)))
    filename = domain + "-output/" + domain + "-IPs.txt" #defining the filename
    final = Counter(final_ips)
    # if directory doesnot exists create it 
    if len(cnt) > 0:
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # a check to protect againsts the Racecondition issues
                if exc.errno != errno.EEXIST:
                    raise
        # if the file already exists , empty the file, this happens when you run the scan against same target multiple times
        with open(filename, 'w') as empty:
            empty.write('')
    
        # writing the IPs in file
        for i in final.keys():
            with open(filename, "a") as f:
                f.write(i + "\n")
        print("   " + second_sub +"[+] IPs saved in                     : {} ".format(filename))

    print("   " + second_sub + "[+] IP scan finished ")


def subdomain_finder(url, domain, r):
    """
        Finding subdomains from web-archive
        Input:
            url: str. This is web.archive.org URL we are using to find info about target
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
    subdomain_pattern = '[0-9a-z]+\.'+domain #matching subdomains 
    subdomains = re.findall(subdomain_pattern , r.text)
    cnt = Counter(subdomains) # using counter for removing duplicate entries 
    print("   " + second_sub + "[+] Total unique subdomains found    : " + str(len(cnt))) # printing no of unique subdomains
    filename = domain + "-output/" + domain + "-subdomains.txt" #defining the filename
    # if directory doesnot exists create it 
    if len(cnt) > 0:
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # a check to protect againsts the Racecondition issues
                if exc.errno != errno.EEXIST:
                    raise
        # if the file already exists , empty the file, this happens when you run the scan against same target multiple times
        with open(filename, 'w') as empty:
            empty.write('')

        # writing the subdomains in file
        for i in cnt.keys():
            with open(filename, "a") as f:
                f.write(i+"\n")
        print("   " + second_sub + "[+] Subdomains saved in              : {} ".format(filename))

    print("   " + second_sub + "[+] Subdomain scan finished ")

def find_secret_tokens(url, domain, data):
    """
        Input:
            url: str. This is web.archive.org URL we are using to find info about target
            domain: str: target domain name
            r: Web archive response
        Output: All data that has valid token syntax
    """
    first_sub = ' \u001b[32m|\u001b[0m'
    second_sub = '\u001b[32m|--\u001b[0m'
    print("\n\u001b[32m  [~] Secret Keys enumeration started\u001b[0m")
    print(" \u001b[32m  |")

    # for amazon secrets : 
    amazon_secrets(data, domain)
    #for facebook Access token   
    facebook_access(data, domain) 
    # for facebook oath tokens 
    facebook_oath(data, domain )
    #facebook_secrets(data , domain)
    # for google api key 
    google_api(data, domain)