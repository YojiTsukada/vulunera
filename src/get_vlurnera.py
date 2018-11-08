import os 
import urllib.request
import xml.etree.ElementTree as ET
# pip install xmltodict
import xmltodict
import json


url = 'https://jvndb.jvn.jp/myjvn?method=getVulnOverviewList&feed=hnd'

with urllib.request.urlopen(url) as response:
    XmlData = response.read()

# Xml to Dictionary
dict = xmltodict.parse(XmlData)

#result = json.dumps(dict,indent=2,ensure_ascii=False)

# Create Lists
newtopics = dict['rdf:RDF']['item']

# Count list
count = len(newtopics)

print('取得件数:' + str(count) + '件')

issues = {}
i = 0 

for topic in newtopics:
    print(topic['title'])
    print(topic['link'])
    print(topic['description'])
    #print(topic['sec:references'][0]['@id'])
    print('-------------------------------------------------------')
