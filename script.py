import requests
import time
url = "https://research.northumbria.ac.uk/irs/"
response = requests.get(url, verify=False)
print(response.status_code)
