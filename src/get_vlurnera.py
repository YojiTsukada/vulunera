import os 
import urllib.request
import xml.etree.ElementTree as ET
# pip install xmltodict
import xmltodict
import json

url = 'https://jvndb.jvn.jp/myjvn?method=getVulnOverviewList&feed=hnd'

with urllib.request.urlopen(url) as response:
    XmlData = response.read()

dict = xmltodict.parse(XmlData)

result = json.dumps(dict,indent=2,ensure_ascii=False)

print(result)
