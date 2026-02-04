import requests
from datetime import datetime

# List of websites to check
WEBSITES = [
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://api.github.com"
]

RETRIES = 3  # Number of retries per site

def check_website(url):
    for attempt in range(1, RETRIES + 1):
        try:
            start = datetime.now()
            response = requests.get(url, timeout=5)
            end = datetime.now()
            response_time = round((end - start).total_seconds() * 1000, 2)  # in ms

            if response.status_code == 200:
                print(f"{end} | ✅ UP | {url} | {response_time} ms")
                return True
            else:
                print(f"{end} | ⚠️ WARNING | {url} returned {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"{datetime.now()} | ❌ DOWN | {url} | Attempt {attempt} failed: {e}")

    print(f"{datetime.now()} | 🚨 {url} is unreachable after {RETRIES} attempts")
    return False

print("=== Website Health Check Started ===")

# Single quick pass for online compiler
for site in WEBSITES:
    check_website(site)

print("=== Health Check Completed ===")
