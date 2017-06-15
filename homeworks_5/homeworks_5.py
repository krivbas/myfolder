import requests

url = "https://httpbin.org/post"
first_name = "Petja"
last_name = "Vasja"
email = "test@gmail.com"
password = "testpass"
r = requests.post(url, {"first_name": first_name, "last_name": last_name, "email": email, "password": password})
data = r.json()
print(data["form"])