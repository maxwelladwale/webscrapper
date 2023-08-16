import enum
from bs4 import *
import requests as rq
import os
# your page url here
r2 = rq.get("https://www.asbo.co.ke/")
soup2 = BeautifulSoup(r2.text, "html.parser")

links = []

# Image folder url here
x = soup2.select('img[src^="https://asbo.co.ke/wp-content/uploads/2021/10/"]')

scheme = "https://nyericlub.com"
for img in x:
    links.append(scheme + img['src'])

for l in links:
    print(l)

# Create folder to store photos
os.mkdir('asbophotos')
i = 1

for index, img_link in enumerate(links):
    if i <=500:
        img_data = rq.get(img_link).content
        # image folder here
        with open("asbophotos\\" + str(index+1)+'.jpg', 'wb+') as f:
            f.write(img_data)
        
        i += 1
    else:
        f.close()
        break

