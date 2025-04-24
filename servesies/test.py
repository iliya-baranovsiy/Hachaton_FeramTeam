import requests

url = "https://api.hh.ru/vacancies?search_field=name&search_field=description&text=Java"

resp = requests.get(url)
response = resp.json()
count = 0
for i in response['items']:
    count+=1

print(count)