import requests
from bs4 import BeautifulSoup
import pandas as pd







# Basic Demonstration of BeautifulSoup methods...

# with open("sample.html", "r") as f:
#     html_doc = f.read();
    

# soup = BeautifulSoup(html_doc,'html.parser')
# # print(soup.prettify())

# # Getting all anchor tags from the html file(sample.html)...
# # print(soup.find_all('a'))


# # Getting the Links and text of all the anchor tags....
# # for link in soup.find_all('a'):
# #     print(link.get('href'))
# #     print(link.get_text())    
    

# # Printing all the childrens of class="container"...
# # for child in soup.find(class_="container").children:
# #     print(child)




# Proxy Setup for obtaining rotating IP's...U can find this on the `ZenRows` documentation...refer - `https://app.zenrows.com/builder`.....
url = "https://httpbin.io/anything"
proxy = "Replace this with your proxy Link"
proxies = {"http": proxy, "https": proxy}
response = requests.get(url, proxies=proxies, verify=False)
    


# Setting this headers is necessary - as some website may detect you scraping there data....so using this headers in your request will mimic a typical browser request...by stimulating the browser...you can make your requests appear as if they are coming from a genuine browser....
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}





# We will be scraping the data from the flipkart website....our target search will be `redmi phones under 35k`...



# Demonstrating for single Page...
url = "https://www.flipkart.com/search?q=redmi%20phones%20under%2035k&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


# Sending request to the url with the proxy setup and headers
r = requests.get(url, proxies=proxies, verify=False, headers=headers)

# Now this object `soup` contains all the HTML data...we can fetch anything using this object....
soup = BeautifulSoup(r.text,'html.parser')
# print(soup.prettify())


# Finding a particular Class..
# You can find this class by inspecting the page html code....if you find the class for one page...it will be same for all other pages as well...
x = soup.find(class_="_4rR01T")
print(x)

# Creating list to store the name and price for the items...
names = []
cost = []
for item in soup.find_all(class_="_4rR01T"):
    names.append(item.text)
    


for price in soup.find_all(class_="_30jeq3 _1_WHN1"):
    cost.append(price.text)
    


dict = {"Name":names , "Price":cost}
    
# Creating a DataFrame for the above data....
df = pd.DataFrame(dict)


df.to_excel("data.xlsx",index=False)







# For multiple Pages - 
names = []
cost = []

# using for loop to access the first 14 pages...making request to each page...and then fetching the name of the product and the price and storing it in the list....
for i in range(1,15):
    url = f"https://www.flipkart.com/search?q=redmi+phones+under+35k&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}"
    
    r = requests.get(url, headers=headers, proxies=proxies, verify=False)
    soup = BeautifulSoup(r.text,'html.parser')
    
    
    
    for item in soup.find_all(class_="_4rR01T"):
        names.append(item.text)
        
    for price in soup.find_all(class_="_30jeq3 _1_WHN1"):
        cost.append(price.text)
        
    

# Converting it into a dataframe and later to an excel file...
dict = {"Name":names, "Price":cost}
df = pd.DataFrame(dict)
df.to_excel("fullDataNew.xlsx",index=False)