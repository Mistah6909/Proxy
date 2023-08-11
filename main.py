import requests
from pathlib import Path
class Proxy:
    # initializes an object with a list of proxies that can either be in a file or a dictionary.
    # If it isnt given a file or a list it will default to a list of around 1000 proxies from the local proxies.txt.
    # Please note that unless this package is being used on a server the proxies will be hosted on your machine.
    def __init__(self,proxies,):
        super.__init__()
        #These statements check whether the proxies are in file or dictionary format.
        if proxies == type(dict):
            proxies = proxies
        if 

    def start_session(self):
        pass
