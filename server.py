import pymysql
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import neural_style as ns
from PIL import Image
import matplotlib.pyplot as plt
from torchvision.utils import save_image

port = 8000

class my_handler(BaseHTTPRequestHandler):

    def _set_header(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()


    def _key_value_parser(self, lists):
        set_ = {}

        for list in lists:
            temp = list.split('=')
            set_[temp[0]] = temp[1]

        return set_


    #create
    def do_POST(self):
        self._set_header()

        path = self.path
        if '?' in self.path:
            urls = self.path.split('?',2)
            request = urls[0]
            kv = urls[1].split('&')

        kv = self._key_value_parser(kv)

        if(request == '/synthesizing'):
            cnn, cnn_normalization_mean, cnn_normalization_std, style_img, content_img, input_img = ns.set_neural_style(kv['content_image'], kv['style_image'])
            output = ns.run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,
                                content_img, style_img, input_img)

            save_img = output[0]
            output_name = '{}x{}.jpg'.format(kv['style_image'], kv['content_image'])
            save_image(save_img, './data/images/output/{}'.format(output_name))

            self.wfile.write('{}'.format(output_name).encode('utf-8'))

            print('synthesizing')
            print('\n\n')

def run():
    httpd = HTTPServer(('localhost', port), my_handler)
    print('Server running on port : {}'.format(port))
    httpd.serve_forever()

run()
