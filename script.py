import requests

response = requests.get("https://www.google.com")
print("✅ GitHub Action ran with requests!")
print("Status code:", response.status_code)


