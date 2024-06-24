import requests
import termcolor

def ch(r):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code} \n", "light_magenta"))
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored(f"Request failed with status code {x.status_code}\n", "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("[+] ", "blue")+termcolor.colored("I cant see ({})!! Maybe it is not work \n".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("[+] ", "blue")+termcolor.colored("there is an Invalid Header | review H.json \n", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("[+] ", "blue") + termcolor.colored("there is a TooManyRedirects Error \n", "red"))
