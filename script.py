import requests

response = requests.get("https://httpbin.org/get")
print("✅ GitHub Action ran with requests!")
print("Status code:", response.status_code)

