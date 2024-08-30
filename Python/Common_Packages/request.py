import requests

x = requests.get('https://docs.python-requests.org/en/latest/user/quickstart/#passing-parameters-in-urls')

print(x.text)