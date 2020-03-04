import requests
import os

def connector(url):
    result = False
    try:
        # TODO control request headers in here
        response = requests.get(url, timeout=30)
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
            print("\u001b[31;1mCan not get target information[0m")
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
    result_folder = os.environ['HOME'] + "/.archivefuzz/" + domain + "-output"
    if not os.path.exists(result_folder):
        print("\n\u001b[32m  Creating result at %s\u001b[0m" % (result_folder))
        os.makedirs(result_folder)
    return result_folder


def report_generator(folder, filename, data):
    report_file = folder + "/" + filename
    try:
        with open(report_file, 'w') as writer:
            writer.write(data)
        print("[+] %s saved in %s" %(filename, report_file)) # TODO edit here
    except:
        pass  # TODO edit here