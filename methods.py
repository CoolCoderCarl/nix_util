import json
import sys

import requests

import parser_description

base_url = "http://httpbin.org/"

main_parser = parser_description.create_parser()
namespace = main_parser.parse_args(sys.argv[1:])


def get_request():
    if namespace.header:
        response = requests.get(base_url + "/headers")
        print(response.text)
    elif namespace.ip:
        response = requests.get(base_url + "/ip")
        json_code = json.loads(response.text)
        print(json_code["origin"])
    elif namespace.useragent:
        response = requests.get(base_url + "/user-agent")
        json_code = json.loads(response.text)
        print(json_code["user-agent"])


def post_request():
    if namespace.header:
        response = requests.post(
            base_url + "/response-headers?freeform=" + namespace.header
        )
        print(response.text)
    elif namespace.delay:
        response = requests.post(base_url + "/delay/" + namespace.delay)
        print(response.text)


def put_request():
    if namespace.status:
        response = requests.put(base_url + "/status/" + namespace.status)
        print(response.text)
    elif namespace.anything:
        response = requests.put(base_url + "/anything")
        print(response.text)


def delete_request():
    if namespace.delete:
        response = requests.delete(base_url + "/delete")
        json_code = json.loads(response.text)
        print(json_code["url"])
