from archivefuzz import *
from urllib.parse import unquote 
import time
import sys
import os
start_time = time.time()

'''
Dont be a jerk use responsibly
'''


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