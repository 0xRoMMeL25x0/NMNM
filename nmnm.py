
try :
    import termcolor
    import requests
    import json
    import sys
    import os 
    import datetime
    from bs4 import BeautifulSoup
except ImportError:
    print("There is an Error in Import the Moduels")
    print("Please Install the Required Modules ( pyfiglet | termcolor | requests | json | datetime)")
    print("or Exexute the Setup.py File ")
    


def banner() :
    banner = """

 _   _ __  __                _   _ __  __    
| \\ | |  \\/  |            | \\ | |  \\/ |            
|  \\| | |\\/| |0xRoMMeL25x0|  \\| | |\\/||
| |\\  | |  | |             | |\\  | |  | | 
|_| \\_|_|  |_|             |_| \\_|_|  |_| 


""" 
    print(banner)
    print(termcolor.colored("[+] ", "blue"), termcolor.colored("NMNM -- V 1.2 By 0xRoMMeL25x0 [{}] ".format(datetime.datetime.now().ctime()), "dark_grey"))
    print(termcolor.colored("[+] ", "blue"), termcolor.colored("Simple tool to create and send requests, read response and Some of Web Scrping ", "dark_grey")) 
    print(termcolor.colored("[+] ", "blue"), termcolor.colored("You Can Edit The Requests HTTP headers From /moduels/request/H.json File", "red"))
    print(termcolor.colored("[+] ", "blue"), termcolor.colored("If you encounter any problem, make sure to install the important Moduels in the requirements file or Execute Setup.py file and do not use root mode in Linux ", "red"))
    print("\n")
banner()


def help():
    help = """

NMNM        Simple Tool to use in create and send HTTP requests and read the resposne
Usage:      python nmnm.py -option <values>

---- Warnning -------
- the url Format Should be like that 
- https://www.example.com
- http://www.example.com
**The HTTP Header request configration in H.json file**
**All outputs will be saved in outputs folder**
**If you want save output of any option just print it Capital** 
-Examples :
python nmnm.py -s https://www.example.com ---> not save
python nmnm.py -S https://www.example.com example html --> will save 

--Tool Options--
-h,         help  Show this help message
-v,         version  Show the version of the tool

--Request Options--
-ch,        check if the target on or not 
-r,         request  Send a HTTP request with the headers from /moduels/request/H.json file
-rsh        request by headers in /moduels/request/H.json and get the response headers
-rs         simple request and get response headers
-Examples:
python nmnm.py -ch  <url>
python nmnm.py -r   <url>
python nmnm.py -rs  <url>
python nmnm.py -rsh <url>

-- reapete the request-- 
--counter-- 
-rc    <url>  <number of req>
-rshc  <url>  <number of req>
-rsc   <url>  <number of req> 


--Source code--
-s          print the source page of target 
-S          put the source code in file 

---Some of Web Scrping---
-t          get the title page of the target <title>
-f          get the forms of the target | <form>
-a          get the links of the target | <a>
-i          get the images of the target  | <img>
-inp        get all input fields of the target
-j          get all script tags of the target | <script> tags
-l          get all link tags of the target | <link> tags  

--Save Output--
-F          get the forms of the target and save it in file | <form>
-A          get the links of the target and save it in file | <a>
-I          get the images of the target and save it in file | <img>
-INP        get all input fields of the target and save it in file | <input>
-J          get all script tags of the target and save it in file | <script> 
-L          get all link tags of the target and save it in file | <link>   


---Notes---
**The HTTP Header request configration in H.json file**
**All outputs will be saved in /outputs folder**
**If you want save output of any option just print it Capital**  
**there is a PHP Version From this tool you will be available soon**

"""
    print(help)


def version():
    version = "V 1.2 | By 0xRoMMeL25x0 \n"
    print(version)

try :
    for order in sys.argv:
        if order == "-h" :
            help()
        if order == "-v" :
            version()
        elif "-ch" in sys.argv:
            from ch import ch 
            url =  sys.argv[sys.argv.index("-ch")+1]
            ch(url)
            break
        elif "-r" in sys.argv:
            from rq import r
            url =  sys.argv[sys.argv.index("-r")+1]
            r(url)
            print("\n")
            break
        elif "-rs" in sys.argv:
            from rq import rs
            url =  sys.argv[sys.argv.index("-rs")+1]
            rs(url)
            print("\n")
            break
        elif "-rsh" in sys.argv:
            from rq import rsh
            url =  sys.argv[sys.argv.index("-rsh")+1]
            rsh(url)
            print("\n")
            break
        elif "-rc" in sys.argv :
            from rq import r 
            url =  sys.argv[sys.argv.index("-rc")+1]
            count  =  sys.argv[sys.argv.index("-rc")+2]
            for x in range(0, int(count)):
                r(url)
            print("\n")
            break 
        elif "-rshc" in sys.argv :
            from rq import rsh 
            url =  sys.argv[sys.argv.index("-rshc")+1]
            count  =  sys.argv[sys.argv.index("-rshc")+2]
            for x in range(0, int(count)):
                rsh(url)
            print("\n")
            break 
        elif "-rsc" in sys.argv :
            from rq import rs 
            url =  sys.argv[sys.argv.index("-rsc")+1]
            count  =  sys.argv[sys.argv.index("-rsc")+2]
            for x in range(0, int(count)):
                rs(url)
            print("\n")
            break 
        elif "-s" in sys.argv:
            from webS import s
            url =  sys.argv[sys.argv.index("-s")+1]
            s(url)
            print("\n")
            break
        elif "-S" in sys.argv:
            from webS import S
            try :
                url =  sys.argv[sys.argv.index("-S")+1]
                filename =  sys.argv[sys.argv.index("-S")+2]
                ex =  sys.argv[sys.argv.index("-S")+3]
                S(url, filename, ex)
                print("\n")
                break
            except :
                print(termcolor.colored("[+] ", "blue"), "Usage: python nmnm.py -S <url> <filename> <extintion> \n")
                break
                
        elif "-t" in sys.argv:
            from webS import t
            url =  sys.argv[sys.argv.index("-t")+1]
            t(url)
            print("\n")
            break
        elif "-f" in sys.argv:
            from webS import f
            url =  sys.argv[sys.argv.index("-f")+1]
            f(url)
            print("\n")
            break
        elif "-F" in sys.argv:
            from webS import F
            try :
                url =  sys.argv[sys.argv.index("-F")+1]
                filename =  sys.argv[sys.argv.index("-F")+2]
                ex =  sys.argv[sys.argv.index("-F")+3]
                F(url, filename, ex)
                print("\n")
                break
            except :
                print(termcolor.colored("[+] ", "blue"), "Usage: python nmnm.py -F <url> <filename> <extintion> \n")
                break
        elif "-a" in sys.argv:
            from webS import a
            url =  sys.argv[sys.argv.index("-a")+1]
            a(url)
            print("\n")
            break
        elif "-A" in sys.argv:
            from webS import A
            try :
                url =  sys.argv[sys.argv.index("-A")+1]
                filename =  sys.argv[sys.argv.index("-A")+2]
                ex =  sys.argv[sys.argv.index("-A")+3]
                A(url, filename, ex)
                print("\n")
                break
            except :
                print(termcolor.colored("[+] ", "blue"), "Usage: python nmnm.py -A <url> <filename> <extintion> \n")
                break
        elif "-i" in sys.argv:
            from webS import i
            url =  sys.argv[sys.argv.index("-i")+1]
            i(url)
            print("\n")
            break
        elif "-I" in sys.argv:
            from webS import I
            try :
                url =  sys.argv[sys.argv.index("-I")+1]
                filename =  sys.argv[sys.argv.index("-I")+2]
                ex =  sys.argv[sys.argv.index("-I")+3]
                I(url, filename, ex)
                print("\n")
                break
            except :
                print(termcolor.colored("[+] ", "blue"), "Usage: python nmnm.py -I <url> <filename> <extintion> \n")
                break
        elif "-inp" in sys.argv:
            from webS import inp
            url =  sys.argv[sys.argv.index("-inp")+1]
            inp(url)
            print("\n")
            break
        elif "-INP" in sys.argv:
            from webS import INP
            try :
                url =  sys.argv[sys.argv.index("-INP")+1]
                filename =  sys.argv[sys.argv.index("-INP")+2]
                ex =  sys.argv[sys.argv.index("-INP")+3]
                INP(url, filename, ex)
                print("\n")
                break
            except :
                print(termcolor.colored("[+] ", "blue"), "Usage: python nmnm.py -INP <url> <filename> <extintion> \n")
                break
        elif "-j" in sys.argv:
            from webS import j
            url =  sys.argv[sys.argv.index("-j")+1]
            j(url)
            print("\n")
            break
        elif "-J" in sys.argv:
            from webS import J
            try :
                url =  sys.argv[sys.argv.index("-J")+1]
                filename =  sys.argv[sys.argv.index("-J")+2]
                ex =  sys.argv[sys.argv.index("-J")+3]
                J(url, filename, ex)
                print("\n")
                break
            except :
                print(termcolor.colored("[+] ", "blue"), "Usage: python nmnm.py -J <url> <filename> <extintion> \n")
                break
        elif "-l" in sys.argv:
            from webS import l
            url =  sys.argv[sys.argv.index("-l")+1]
            l(url)
            print("\n")
            break
        elif "-L" in sys.argv:
            from webS import L
            try :
                url =  sys.argv[sys.argv.index("-L")+1]
                filename =  sys.argv[sys.argv.index("-L")+2]
                ex =  sys.argv[sys.argv.index("-L")+3]
                L(url, filename, ex)
                print("\n")
                break
            except :
                print(termcolor.colored("[+] ", "blue"), "Usage: python nmnm.py -L <url> <filename> <extintion> \n")
                break
        else :
            help()
                
        
except KeyboardInterrupt:
    print("Goodbye")
    exit()
except json.decoder.JSONDecodeError:
    print(termcolor.colored("[+] ", "blue"), "there is an Error in H.json file | reveiw it \n")
except :
    help()    
    exit()
