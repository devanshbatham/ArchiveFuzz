import requests
import os
import re


def connector(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion'
    }
    result = False
    try:
        # TODO control request headers in here
        response = requests.get(url,headers=headers ,timeout=30)
        result = response.text
    except requests.ConnectionError as e:
        raise ConnectionError("\u001b[31;1mCan not connect to server. Check your internet connection\u001b[0m")
    except requests.Timeout as e:
        raise TimeoutError("\u001b[31;1mOOPS!! Timeout Error\u001b[0m")
    except requests.RequestException as e:
        raise AttributeError("\u001b[31;1mError in HTTP request\u001b[0m")
    except KeyboardInterrupt:
        raise KeyboardInterrupt("\u001b[31;1mInterrupted by user\u001b[0m")
    except Exception as e:
        raise RuntimeError("\u001b[31;1m%s\u001b[0m" % (e))
    finally:
        if not result:
            print("\u001b[31;1mCan not get target information\u001b[0m")
            print("\u001b[31;1mIf you think this is a bug or unintentional behaviour. Report here : https://github.com/devanshbatham/ArchiveFuzz/issues\u001b[0m")
        return result


def prepare_result(domain):
    """
        Create a folder at home
        The format should be like "/home/user/.archivefuzz/domain-output/"
        domain: str: target domain name
        result_folder: string full path of folder to save files
    """
    # Might not work on windows system
    if os.name == "nt":
        result_folder = domain + "-output"
    else:
        result_folder = os.environ['HOME'] + "/.archivefuzz/" + domain + "-output"
    if not os.path.exists(result_folder):
        print("\n\u001b[32m  Creating result at %s\u001b[0m" % (result_folder))
        os.makedirs(result_folder)
    return result_folder


def report_generator(folder, filename, data):
    report_file = folder + "/" + filename + ".txt"
    try:
        with open(report_file, 'w') as writer:
            writer.write(data)
        print("      [!] Saved in %s" %(report_file))
    except OSError as e:
        print("\u001b[31;1m%s[0m" % (e))
        raise OSError("\u001b[31;1mError while writing %s[0m" % (report_file))


def info_gatherer(data, task_name, patterns):
    task_pattern, blacklist_pattern = patterns
    """
        Template function to gather all token format
        data: string = response from web.archive
        task_pattern: regex pattern of token
        task_name: name of token to get (facebook api, facebook_auth)
        blacklist_pattern: Any string should be removed
    """
    print("\n\u001b[32m  [*] %s scan started" % (task_name))
    print("\u001b[32m   |")
    second_sub = '\u001b[32m|--\u001b[0m'
    if blacklist_pattern:
        r = re.sub(blacklist_pattern, '', data)
        results = set(re.findall(task_pattern , r))
    else:
        if task_name.startswith("IPv"):
            results = re.findall(task_pattern, data)
            results = set([".".join(octet) for octet in results])
        else:
            results = set(re.findall(task_pattern, data))
    print("   %s[+] %-30s: %s" % (second_sub, task_name, len(results)))
    return list(results)
