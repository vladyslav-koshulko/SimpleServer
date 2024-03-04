# This is a sample Python script.
import json
import os.path
import http.server
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

# def run(serverClass=HTTPServer, handlerClass=BaseHTTPRequestHandler):
#     serverAddress = ('', 8080)
#     httpd = serverClass(serverAddress, handlerClass)
#     try:
#         httpd.serve_forever()
#     except KeyboardInterrupt:
#         httpd.server_close()


def dir_to_json(path):
    data = []
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            data.append({"name": item})
        else:
            data.append({"name": item})
    return data




class HttpRequestHandler(BaseHTTPRequestHandler):

    def get_response(self):
        s = dir_to_json(os.curdir)
        return json.dumps(s)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(self.get_response().encode())

    def do_POST(self):
        self.do_GET()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    server = HTTPServer(("0.0.0.0", 8080), HttpRequestHandler)
    server.serve_forever()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
