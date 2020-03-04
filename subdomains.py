from collections import Counter
import re
import os
import errno

# status :  completed
# todo   :  nothing 

# function for finding subdomains from web-archive

def subdomain(url, domain, r):
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
