import sys
import parserDescription
import requests
import json

base_url='http://httpbin.org/'

main_parser = parserDescription.createParser()
namespace = main_parser.parse_args(sys.argv[1:])

def getRequest():
    if namespace.header:
        response = requests.get(base_url + '/headers')
        print(response.text)
    elif namespace.ip:
        response = requests.get(base_url + '/ip')
        jsoncode = json.loads(response.text)
        print(jsoncode['origin'])
    elif namespace.useragent:
        response = requests.get(base_url + '/user-agent')
        jsoncode = json.loads(response.text)
        print(jsoncode['user-agent'])

def postRequest():
    if namespace.header:
        response = requests.post(base_url + '/response-headers?freeform=' + namespace.header)
        print(response.text)
    elif namespace.delay:
        response = requests.post(base_url + '/delay/' + namespace.delay)
        print(response.text)

def putRequest():
    if namespace.status:
        response = requests.put(base_url + '/status/' + namespace.status)
        print(response.text)
    elif namespace.anything:
        response = requests.put(base_url + '/anything')
        print(response.text)

def deleteRequest():
    if namespace.delete:
        response = requests.delete(base_url + '/delete')
        jsoncode = json.loads(response.text)
        print(jsoncode['url'])