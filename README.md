# Proxy
A package to help simplify setup and address cycling for webscraping applications.
## A Simple Example Program
to start make or find a list of proxies in a txt file for this example we are using this list of 4 addresses
203.243.63.16:80
3.24.58.156:3128
95.217.104.21:24815
103.151.41.7:80
```python
import Proxy
from urllib import request
from urllib.request import urlopen
# initialize an object of the proxy class with debug enabled to show results, that pulls proxies from the example_proxies.txt file that are all used a max number of 10 times.
proxy = Proxy.Proxy(10, "example_proxies.txt", debug=True)
# manually cycles the proxy to the next in the list
proxy.cycle()
# returns the address to be used in webscraping functions
print(proxy.get_address())
# returns data concerning the current address such as anonymity country and protocol
proxy.get_proxy_data()
# The following block shows how the object automatically cycles IP's to avoid detection
# The number of times a proxy has been used increases whenever the function get_adress is called which may cause it to accidentally cycle. 
# In that case just call for proxy.address() if you need to call the address without acidentally cycling.
for time in range(30):
    req = request.Request(
        "https://webscraper.io/test-sites/e-commerce/allinone")
    req.set_proxy(proxy.get_address(), 'http')
    response = urlopen(req)
```
