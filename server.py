import pymysql
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import ./neural-style/neural-style

port = 8000

class my_handler(BaseHTTPRequestHandler):

    def _set_header(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()


    def _key_value_parser(self, lists):
        set = {}

        for list in lists:
            temp = list.split('=')
            set[temp[0]] = temp[1]

        return set


    #create
    def do_POST(self):
        self._set_header()

        path = self.path
        if '?' in self.path:
            urls = self.path.split('?')
            request = urls[0]
            kv = urls[1].split('&')

        kv = self._key_value_parser(kv)
        print(kv)


        if(request == '/synthesizing'):
            


            print('/synthesizing')
            print('\n\n')



httpd = HTTPServer(('localhost', port), my_handler)
print('Server running on port : {}'.format(port))
httpd.serve_forever()
