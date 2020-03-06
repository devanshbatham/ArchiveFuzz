from archivefuzz import *
from urllib.parse import unquote 
import time
import sys
import os
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
    data = unquote(response) # url decoding the data
    
    # add your api keys here , the form of dict [format : {"taskname" : ["regex pattern"] , [blacklist pattern(if any)]}]

    tasks = {
        "Email": [
            "([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]{2,7})",
            "(-p-|mp4|webm|JPG|pdf|html|jpg|jpeg|png|gif|bmp|svg|1x|2x|3x|4x|5x|6x|7x|9x|10x|11x|12x|13x|14x|15x)"
            ],
        "IPv4": [
            "(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)",
            ""
        ],
        "Subdomain": [
            "[0-9a-z]+\." + domain,
            ""
        ],
        "AWS Access IDs": [
            "(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}",
            ""
        ],
        "Facebook Acess Token": [
            "EAACEdEose0cBA[0-9A-Za-z]+",
            "",
        ],
        "Facebook Oath Token": [
            "[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].*['|\"][0-9a-f]{32}['|\"]",
            ""
        ],
        "Google API Key": [
            "AIza[0-9A-Za-z\\-_]{35}",
            ""
        ]
    }
    for name, patterns in tasks.items():
        result = info_gatherer(data, name, patterns)
        if result:
            report_generator(result_folder, name.lower(), "\n".join(result))
    

    

if __name__ == "__main__":
    if os.name=="nt":
        os.system("cls")
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
