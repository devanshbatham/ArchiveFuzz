from archivefuzz import *
from urllib.parse import unquote 
from archivefuzz.controller import connector
from archivefuzz.controller import prepare_result
import time
import sys
start_time = time.time()

'''
Dont be a jerk use responsibly
'''

def main(domain, result_folder):
    print(" \u001b[34;1m [!] Be patient . This might take some time . I am hunting Archives for you \u001b[0m\n")
    url = "http://web.archive.org/cdx/search/cdx?url=*."
    url += domain + "/*&output=txt&fl=original&collapse=urlkey&page="
    response = connector(url)
    if not response:
        return
    data = unquote(response)                 # url decoding the data 
    subdomain_finder(domain, response)            # for subdomains, imported from subdomains.py
    email_finder(domain, response)  # for emails , imported from emails.py 
    ip_finder(domain, response)            # finds IPv4 addresses , imported from ip_address.py

     # beta state starts here  
    token_finder(domain, response)                                    
    
    # prints the total execution time 

    

if __name__ == "__main__":
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
    result_folder = prepare_result(domain)
    # TODO edit here to make it work with both cli and args
    main(domain, result_folder)
    print("\n \u001b[31m [!] Total execution time                 : %ss\u001b[0m" % str((time.time() - start_time))[:-12])