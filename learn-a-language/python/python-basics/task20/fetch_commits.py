def fetch_commit_history(repo_name):
    url = f"{API_URL}/repos/YOUR_GITHUB_USERNAME/{repo_name}/commits"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            print(commit['commit']['message'])
    else:
        print(f"Failed to fetch commits. {response.json()['message']}")

fetch_commit_history("test-repo")