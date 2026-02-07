from datetime import datetime
import requests
import time

Retries = 3
time_out = 5
retry_time = 2

Websites = {
    "https://google.com",
    "https://github.com"
}

def health_checker(url):
    for attempt in range (1, Retries + 1):
        try:
            start = datetime.now()
            response = requests.get(url, timeout=time_out)
            end = datetime.now()
            reponse_time = round((end - start).total_seconds() * 1000, 2)
            size_kb = round(len(response.content) / 1024, 2)

            if response.status_code == 200:
                print (f"{end} | {url} is UP | Reponse time - {reponse_time} | Size - {size_kb} kb")
                return True
            else:
                print (f"{end} | Warning for {url} | Status - {response.status_code}")
        except requests.exceptions.RequestException as e:
            print (f"{datetime.now()} | {url} is unreachable | Attempt no {attempt}")
        
        time.sleep(retry_time)
    
    print (f"{url} is DOWN | All Attempts are failed")
    return False

Results = {}

for site in Websites:
    Results[site] = health_checker(site)

print ("Summery")
for site, status in Results.items():
    print (f"{site} Status : {'UP' if status else 'DOWN'}  ")