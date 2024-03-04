import json
from http import client


def lookup(baseurl, port):
    http_connection = client.HTTPConnection(baseurl, port, 10)
    http_connection.request("GET", "/")
    response = http_connection.getresponse()
    print(response.read().decode())


def parser(jsonString):
    loads = json.loads(jsonString)
    return loads


lookup1 = lookup("localhost", 8080)
print(type(lookup1))
parser1 = parser(str(lookup1))
print(type(parser1))
print(parser1)
print()
