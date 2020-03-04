from error_handling import error_handler
from subdomains import subdomain
from emails import email_enumerator
from ip_address import find_ip
from secret_tokens import find_secret_tokens
from urllib.parse import unquote 
import requests
import errno
import re
import os
import time
import sys
start_time = time.time()

'''
Dont be a jerk use responsibly
'''

if __name__ == "__main__":
    
    if os.name == 'nt':
        os.system('cls')

    banner = """
\u001b[35;1m
     _____                .__    .__            ___________                    
    /  _  \_______   ____ |  |__ |__|__  __ ____\_   _____/_ __________________
   /  /_\  \_  __ \_/ ___\|  |  \|  \  \/ // __ \|    __)|  |  \___   /\___   /
  /    |    \  | \/\  \___|   Y  \  |\   /\  ___/|     \ |  |  //    /  /    / 
  \____|__  /__|    \___  >___|  /__| \_/  \____ >___  / |____//_____ \/_____\.
          \/            \/     \/              \/    \/              \/      \/ \u001b[0m

                               \u001b[42;1m-coded with <3 by Devansh Batham\u001b[0m

     
    """
    print(banner)
    if len(sys.argv)!=2:
            print("\u001b[31;1m[!] Usage : python3 archivefuzz.py example.com \u001b[0m")
            sys.exit(1) 
    domain = sys.argv[1]
    print(" \u001b[34;1m [!] Be patient . This might take some time . I am hunting Archives for you \u001b[0m\n")
    url = "http://web.archive.org/cdx/search/cdx?url=*."+domain+"/*&output=txt&fl=original&collapse=urlkey&page="
    error_handler(url)                    # for error handling, imported from error_handling.py
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        exit(0)
    data = unquote(r.text)                 # url decoding the data 
    subdomain(url , domain , r)            # for subdomains, imported from subdomains.py
    email_enumerator(url , domain , data)  # for emails , imported from emails.py 
    find_ip(url , domain ,data)            # finds IPv4 addresses , imported from ip_address.py

     # beta state starts here  
    find_secret_tokens(url , domain , data)                                    
                                          # prints the total execution time 


    print("\n \u001b[31m [!] Total execution time                 : %ss\u001b[0m" % str((time.time() - start_time))[:-12])
    