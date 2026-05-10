import requests


get_reponse = requests.get("https://www.nathanielkoloc.com")

print(get_reponse.text)