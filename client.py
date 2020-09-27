import requests

url = "http://localhost:8000/synthesizing"
params = {'content_image':'dog','style_image': 'crying'}

res = requests.post(url, params=params)
print(res)