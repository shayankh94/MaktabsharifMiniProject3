import requests
import json

token = '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'
user = 'shayankh94'
repository = "MaktabsharifMiniProject3"

repository_url = f'https://api.github.com/repos/{user}/{repository}'

commits_url = f'https://api.github.com/repos/{user}/{repository}/commits'

headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github+json',
}

response = requests.get(repository_url, headers=headers)

if response.status_code == 200:
    repository_info = response.json()
    with open('repository.json', 'w') as repo_file:
        json.dump(repository_info, repo_file, indent=4)

    response = requests.get(commits_url, headers=headers)
    commits = response.json()

    commits_by_author = {}
    for commit in commits:
        author = commit['commit']['author']['name']
        if author in commits_by_author:
            commits_by_author[author].append(commit)
        else:
            commits_by_author[author] = [commit]

    with open('commits.json', 'w') as commits_file:
        json.dump(commits_by_author, commits_file, indent=4)

else:
    print(f"Failed : {response.status_code}")
