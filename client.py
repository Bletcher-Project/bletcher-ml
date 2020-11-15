import requests

url = "http://192.168.50.67:8000/synthesizing"
data = {'content_image':'dog','style_image': 'crying'}

res = requests.post(url, data=data)
print(res)
