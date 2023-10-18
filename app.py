import os
import requests

serviceId = os.environ['INPUT_SERVICEID'] # service id i.e 'srv-cknlgo61101c73fL966g'
bearer = os.environ['INPUT_BEARER'] # bearer api token i.e 'rnd_xkQiKVCnuBUzGtySBKKWSX7G14c'

def run():
    url = f"https://api.render.com/v1/services/{serviceId}/deploys"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {bearer}"
    }
    response = requests.post(url, headers=headers)
    print(f"::set-output name=response::{response.text}")

if __name__ == '__main__':
    run()