from collections import Counter
import re
import os

    
def amazon_secrets(data, domain):
    #print(data)
    second_sub = '\u001b[32m|--\u001b[0m'
    # there are three possible keys , below the regex patterns for them 
    aws_client_id_pattern = "(A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}"
    aws_clients = re.findall(aws_client_id_pattern , data)
    cnt = Counter(aws_clients)

    print("   " + second_sub + "[+] AWS Access IDs found             : " + str(len(cnt)))
    filename = domain + "-output/" + domain + "-AWS-ACCESS-IDs.txt"
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

        # writing the aws access ids in file
        
        for i in cnt.keys():
            with open(filename, "a") as f:
                f.write(i + "\n") 
        print("   " + second_sub + "[+] AWS Access IDs saved in          : {} ".format(filename))


def facebook_access(data, domain):
    second_sub = '\u001b[32m|--\u001b[0m'
    
    facebook_access_token_pattern = "EAACEdEose0cBA[0-9A-Za-z]+"
    
    facebook_access_tokens = re.findall(facebook_access_token_pattern, data) 
    cnt = Counter(facebook_access_tokens)

    print("   " + second_sub + "[+] Facebook Access Tokens found     : " + str(len(cnt)))
    filename = domain + "-output/" + domain + "-Facebook-access-tokens.txt"
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

        
        for i in cnt.keys():
            with open(filename, "a") as f:
                f.write(i + "\n") 
        print("   " + second_sub + "[+] Facebook Tokens saved in         : {} ".format(filename))
    
    

def facebook_oath(data, domain):
    # for interactive output
    second_sub = '\u001b[32m|--\u001b[0m'

    facebook_oath_token_pattern = "[f|F][a|A][c|C][e|E][b|B][o|O][o|O][k|K].*['|\"][0-9a-f]{32}['|\"]"
    facebook_oath_tokens = re.findall(facebook_oath_token_pattern , data)
    cnt = Counter(facebook_oath_tokens)
    print("   " + second_sub + "[+] Facebook Oath Tokens found       : " + str(len(cnt)))

    filename = domain + "-output/" + domain + "-Facebook-oath-tokens.txt"
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

        
        for i in cnt.keys():
            with open(filename, "a") as f:
                f.write(i+"\n") 
        print("   " + second_sub + "[+] Facebook Oath Tokens  saved in   : {} ".format(filename))

def google_api(data, domain):
    # for interactive output
    second_sub = '\u001b[32m|--\u001b[0m'

    google_api_pattern = "AIza[0-9A-Za-z\\-_]{35}"
    google_apis = re.findall(google_api_pattern , data)
    cnt = Counter(google_apis)
    print("   " + second_sub + "[+] Google API Keys found            : " + str(len(cnt)))
    
    filename = domain + "-output/" + domain + "-Google-API-keys.txt"
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

        
        for i in cnt.keys():
            with open(filename, "a") as f:
                f.write(i+"\n") 
        print("   " + second_sub + "[+] Google  APIs  saved in           : {} ".format(filename))
    print("   " + second_sub + "[+] API Key scan finished ")
