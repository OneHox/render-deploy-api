import requests

serviceId = 'srv-cknlgo61101c73fL966g'
bearer = 'rnd_xkQiKVCnuBUzGtySBGKKWSX7G14c'

url = f"https://api.render.com/v1/services/{serviceId}/deploys"
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {bearer}"
}

response = requests.post(url, headers=headers)
print(response.text)