import os 
import urllib.request
import xml.etree.ElementTree as ET
# pip install xmltodict
import xmltodict
import json

def lambda_handler(event, context):
    # TODO implement
    url = 'https://jvndb.jvn.jp/myjvn?method=getVulnOverviewList&feed=hnd'

    with urllib.request.urlopen(url) as response:
        XmlData = response.read()

    # Xml to Dictionary
    dict = xmltodict.parse(XmlData)

    # Create Lists
    newtopics = dict['rdf:RDF']['item']

    # Count list
    count = len(newtopics)

    print('取得件数:' + str(count) + '件')

    issues = {}
    i = 0 

    for topic in newtopics:
        issues[i] = {}
        issues[i]['title'] = topic['title']
        issues[i]['link'] = topic['link']
        issues[i]['description'] = topic['description']
        i+=1


    #return json.dumps(issues,ensure_ascii=False)
    return json.dumps(issues,ensure_ascii=False)