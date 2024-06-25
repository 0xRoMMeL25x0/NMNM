import sys
import os 

try :
    import termcolor
    import requests
    import json
    import datetime
    from bs4 import BeautifulSoup
    print("Ok All requirements is Installed")
except ImportError:
    platform = sys.platform
    if platform == "win32":
        os.system("pip install pyfiglet termcolor requests json beautifulsoup4")
        print("Ok All requirements is Installed")
    else :
        os.system("pip3 install pyfiglet termcolor requests json beautifulsoup4")
        print("Ok All requirements is Installed")
        
