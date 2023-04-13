#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
import time
while True:
    r = requests.get("https://api.nobelprize.org/v1/prize.json")
    if r.status_code ==200:
        data=r.json()
        print(data)
    else:
        exit()


# In[ ]:


get_ipython().system('pip install pymongo[srv]')


# In[ ]:


import requests
import time
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:Admin%40123@nobelprize.ktic81z.mongodb.net/NobelPrize?ssl=true&ssl_cert_reqs=CERT_NONE")
db = client.get_database('NobelPrize')
records = db.TestCollection
#db = client.test testcase
while True:
    r=requests.get("https://api.nobelprize.org/v1/prize.json")
    if r.status_code == 200:
        data=r.json()
        print(data)
        records.insert_one(data)
        #time.sleep(60)
    else:
        exit()

