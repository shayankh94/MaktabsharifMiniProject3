import requests


user = 'shayankh94'
url = f'https://api.github.com/users/{user}/repos'
response = requests.get(url)

if response.status_code == 200:
    repositories = response.json()
    for repo in repositories:
        print(repo['name'])
else:
    print(f"Failed: {response.status_code}")

