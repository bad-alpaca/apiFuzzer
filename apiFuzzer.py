import sys
import requests
import argparse

print('''
 █████╗ ██████╗ ██╗                              
██╔══██╗██╔══██╗██║                              
███████║██████╔╝██║                              
██╔══██║██╔═══╝ ██║                              
██║  ██║██║     ██║                              
╚═╝  ╚═╝╚═╝     ╚═╝                              

███████╗██╗   ██╗███████╗███████╗███████╗██████╗ 
██╔════╝██║   ██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗
█████╗  ██║   ██║  ███╔╝   ███╔╝ █████╗  ██████╔╝
██╔══╝  ██║   ██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗
██║     ╚██████╔╝███████╗███████╗███████╗██║  ██║
╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
simple endpoint fuzzer. returns json response, status code, endpoint name.
apiFuzzer.py v1.0.0
Created by: ezra\U0001F999                                                 

''')

parser = argparse.ArgumentParser(description='Endpoint Fuzzer')
parser.add_argument('url', type=str, help='The URL to fuzz')
parser.add_argument('-w', '--wordlist', dest='wordlist', type=str, required=True, help='The path to the wordlist file')
args = parser.parse_args()

try:
    with open(args.wordlist, "r") as wordlist:
        for word in wordlist:
            url = f"{args.url.rstrip('/')}/{word.strip()}"
            try:
                res = requests.get(url)
                if res.status_code == 200:
                    print("[+] Endpoint:", url)
                    print("[+] Status Code:", res.status_code)
                    if res.status_code == 200:
                        try:
                            data = res.json()
                            print("[+] JSON Response:", data)
                        except ValueError as e:
                            print("[-] JSON Decode Error:", e)
            except requests.exceptions.RequestException as e:
                print("[-] Request Error:", e)
except FileNotFoundError as e:
    print("[-] File Not Found Error:", e)
except Exception as e:
    print("[-] Unexpected")
except KeyboardInterrupt:
    print("\nExiting program...")
    sys.exit(0)

