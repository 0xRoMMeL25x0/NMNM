import requests 
import termcolor
import json
import os 


# A request with Headers 
def r(r):
    try:
        headers = {}
        with open("H.json", "r") as f:
            data = json.load(f)
            headers = data
        x = requests.get(r, headers=headers)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code} \n", "light_magenta"))
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored(f"Request failed with status code {x.status_code}", "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))
    




# A resuest with headers and get response headers 
def rsh(r):
    try:
        headers = {}
        with open("H.json", "r") as f:
            data = json.load(f)
            headers = data
        x = requests.get(r, headers=headers)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code} \n", "light_magenta"))
            print(termcolor.colored("Response: \n", "blue"))
            for key, val in x.headers.items():
                print(key, ':', val, "")
            print("\n")
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored(f"Request failed with status code {x.status_code} please review the H.json file ", "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("[+] ", "blue")+termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("there is a TooManyRedirects Error " , "red"))



# A resuest without headers and get response headers 
def rs(r):
    try:
        headers = {}
        with open("H.json", "r") as f:
            data = json.load(f)
            headers = data
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code} \n", "light_magenta"))
            print(termcolor.colored("Response: \n", "blue"))
            for key, val in x.headers.items():
                print(key, ':', val, "")
            print("\n")
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored(f"Request failed with status code {x.status_code}", "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("[+] ", "blue")+termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("[+] ", "blue")+termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("[+] ", "blue") + termcolor.colored("there is a TooManyRedirects Error ", "red"))

