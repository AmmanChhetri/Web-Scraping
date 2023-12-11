# pip install requests
import requests

your_API_key = "get_it_from_website"
url = "https://httpbin.io/anything"
proxy = "http://{your_API_key}:premium_proxy=true&autoparse=true@proxy.zenrows.com:8001"
proxies = {"http": proxy, "https": proxy}
response = requests.get(url, proxies=proxies, verify=False)

# To see the IP Address..this code will rotate the IP on each Run...u can find this in `zenRows` documentation...
# `https://app.zenrows.com/builder`
ip = response.json()["origin"]
print(ip.split(':')[0])