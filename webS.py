import requests
from bs4 import BeautifulSoup
import termcolor
import random 

# get source -s
def s(r):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            print(html_parser.prettify())
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored(f"Request failed with status code {x.status_code} | reveiw Headers file", "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))
    

# s("http://google.com")




# save thr sorce in fiel -S 
def S(r, n, ex):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            soup = BeautifulSoup(x.content, 'html.parser')
            source_code = soup.prettify()
            with open("outputs/{}.{}".format(n, ex), "w", encoding="utf-8") as f:
                f.write(source_code)
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"File has been save successfully \n", "light_magenta"))
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored(f"Request failed with status code {x.status_code} | reveiw Headers file", "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))


# S("https://facebook.com", "mm", "html")







# get page title -t 
def t(r):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            title = html_parser.find("title").text 
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("{} page title is : {}  \n".format(r, title) , "light_magenta"))
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))


# t("https://google.com")


def f(r):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            forms = html_parser.find("form")
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("Here you go : \n " , "light_magenta"))
            print(forms.prettify())        
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))

# f("https://google.com")


def F(r, n, ex):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            forms = html_parser.find("form").prettify()
            file = open("outputs/{}.{}".format(n,ex), "w")
            file.write(str(forms))
            file.close()
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("File has been save successfully \n", "light_magenta"))
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored(f"Request failed with status code {x.status_code} | reveiw Headers file", "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))


# F("https://www.facebook.com", "Facebook", "html")

def a(r):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            links = html_parser.findAll("a")
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("Here you go : \n " , "light_magenta"))
            for a in links :
                print(a)       
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))

# a("https://google.com")

def A(r, n, ex):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.content
            html_parser = BeautifulSoup(html, "html.parser")
            links = html_parser.findAll("a")
            with open("outputs/{}.{}".format(n, ex), "w", encoding="utf-8") as f:
                for a in links:
                    f.write(str(a) + "\n")

            print(termcolor.colored("[+] ", "blue"), termcolor.colored("File has been save successfully \n" , "light_magenta"))
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))

# A("https://google.com", "google_a", "txt")



def i(r):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            images = html_parser.findAll("img")
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("Here you go : \n " , "light_magenta"))
            for i in images :
                print(str(i) + "\n")       
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))


# i("https://google.com")



def I(r, n, ex):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            images = html_parser.findAll("img")
            with open("outputs/{}.{}".format(n, ex), "w", encoding="utf-8") as f:
                for a in images:
                    f.write(str(a) + "\n")
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("File has been save successfully \n" , "light_magenta"))
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))


# I("https://facebook.com", "img_facebook", "txt")


def inp(r):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            inputs = html_parser.findAll("input")
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("Here you go : \n " , "light_magenta"))
            for i in inputs :
                print(str(i) + "\n")       
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))


# inp("https://google.com")



def INP(r, n, ex):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            inputs = html_parser.findAll("input")
            with open("outputs/{}.{}".format(n, ex), "w", encoding="utf-8") as f:
                for a in inputs:
                    f.write(str(a) + "\n")
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("File has been save successfully \n" , "light_magenta"))
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))


# INP("https://facebook.com", "img_facebook", "txt")



def j(r):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            jses = html_parser.findAll("script")
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("Here you go : \n " , "light_magenta"))
            for i in jses :
                print(str(i) + "\n")       
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))


def J(r, n, ex):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            jses = html_parser.findAll("script")
            with open("outputs/{}.{}".format(n, ex), "w", encoding="utf-8") as f:
                for a in jses:
                    f.write(str(a) + "\n")
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("File has been save successfully \n" , "light_magenta"))
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))

def l(r):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            links = html_parser.findAll("link")
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("Here you go : \n " , "light_magenta"))
            for i in links :
                print(str(i) + "\n")       
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))


def L(r, n, ex):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            links = html_parser.findAll("link")
            with open("outputs/{}.{}".format(n, ex), "w", encoding="utf-8") as f:
                for a in links:
                    f.write(str(a) + "\n")
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("File has been save successfully \n" , "light_magenta"))
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))


def ide(r, e, id):
    try:
        x = requests.get(r)
        if x.status_code == 200:
            print(termcolor.colored("[+] ", "blue"), termcolor.colored(f"Request sent successfully with status code {x.status_code}  \n", "light_magenta"))
            html = x.text
            html_parser = BeautifulSoup(html, "html.parser")
            Element = html_parser.find(e,  attrs={"id" : id})
            print(termcolor.colored("[+] ", "blue"), termcolor.colored("Found it"))       
            print(Element)        
        else :
            print( termcolor.colored("[+] ", "blue") , termcolor.colored("Request failed with status code {} | reveiw Headers file".format(x.status_code), "red"))
    except requests.exceptions.ConnectionError :
        print( termcolor.colored("I cant see ({})!! Maybe it is not work ".format(r), "red"))
    except requests.exceptions.MissingSchema :
        print( termcolor.colored("[+] ", "blue")+ termcolor.colored("Invalid URL ", "red")+ termcolor.colored("Did you ment https://{} or http://{}?".format(r,r)) + "\n")
    except requests.exceptions.InvalidHeader:
        print( termcolor.colored("there is an Invalid Header ", "red"))
    except requests.exceptions.TooManyRedirects:
        print( termcolor.colored("there is a TooManyRedirects Error " , "red"))

