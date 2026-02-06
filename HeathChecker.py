import requests
from datetime import datetime

websites = [
    "https://google.com"
]

retries = 3

def healthCheck(url):
    for attempt in range (1, retries + 1):
        try:
            start = datetime.now()
            response = requests.get(url, timeout=2)
            end = datetime.now()
            response_time = round((end-start).total_seconds() * 1000, 2)

            if response.status_code == 200:
                print (f"{end} | {url} is UP with response time {response_time}")
                return True
            else:
                print (f"{end} | Warning for {url} the status is {response.status_code}")
        except requests.exceptions.RequestException as e:
            print (f"{datetime.now()} | Received exception for {url} exception - {e}")
    print (f"{datetime.now()} | {url} is unreachable, Attempt no. {attempt}")
    return False

for site in websites:
    healthCheck(site)
