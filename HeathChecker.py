from datetime import datetime
import requests
import time

retries = 3
time_out = 5
retry_delay = 2

websites = [
    "https://google.com",
    "https://github.com"
]

def health_checker(url):
    for attempt in range(1, retries +1):
        try:
            start = datetime.now()
            response = requests.get(url, timeout= time_out)
            end = datetime.now()
            response_time = round((end - start).total_seconds() * 1000, 2)
            size_kb = round(len(response.content) / 1024, 2)

            if response.status_code == 200:
                print(f"{end} | {url} is UP | Response time is {response_time} | size is {size_kb} kb")
                return True
            else:
                print (f"{end} | Warning for {url} | Status is {response.status_code}")
            
        except requests.exceptions.RequestException as e:
            print (f"{datetime.now()} | {url} is unreachable | Attempt no {attempt} | Exception {e}")
        
        time.sleep(retry_delay)
    print (f"{datetime.now()} | {url} is DOWN | All attempts are failed.")
    return False

results = {}

for site in websites:
    results[site] = health_checker(site)

print("Summary")
for site, status in results.items():
    print(f"{site} : Status is {'UP' if status else 'DOWN'}")
