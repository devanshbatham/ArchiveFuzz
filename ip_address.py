from collections import Counter
import re
import os
import errno

# status :  completed
# todo   :  nothing

# Note   : This function might produce some false positives , but in most the cases the results are correct
# function for enumerating IPv4 addresses

def find_ip(url, domain, data):

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
