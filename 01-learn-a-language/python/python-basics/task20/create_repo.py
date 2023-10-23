import requests

TOKEN = 'YOUR_PERSONAL_ACCESS_TOKEN'
HEADERS = {
    'Authorization': f'token {TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}
API_URL = 'https://api.github.com'

def create_repo(repo_name):
    url = f"{API_URL}/user/repos"
    data = {
        "name": repo_name,
        "description": "Repository created via API",
        "auto_init": True  # This will initialize the repo with a README.md
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"Repository {repo_name} created successfully!")
    else:
        print(f"Failed to create the repository. {response.json()['message']}")

create_repo("test-repo")