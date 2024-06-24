import sys
import os 

try :
    import termcolor
    import requests
    import json
    import datetime
    from bs4 import BeautifulSoup
except ImportError:
    platform = sys.platform
    if platform == "win32":
        os.system("pip install pyfiglet termcolor requests json beautifulsoup4")
    else :
        os.system("pip3 install pyfiglet termcolor requests json beautifulsoup4")
        