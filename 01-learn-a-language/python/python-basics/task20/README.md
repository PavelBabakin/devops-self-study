# Task 20: Use Python to interact with the GitHub API: create a repository, commit a file, and fetch commit history.

## **Automating GitHub Tasks with Python: A Step-by-Step Guide**

In the modern era of DevOps and continuous integration, automation is king. While GitHub provides an intuitive interface for managing repositories, there are times when a more programmatic approach is desired. Enter Python, a versatile language that, when combined with the GitHub API, can supercharge your repository management tasks. In this article, we'll delve into automating common GitHub tasks using Python.

### **Prerequisites**

Before we embark on our automation journey, ensure you have the following:

- Python installed on your machine.
- The **`requests`** library, which can be installed via pip:

```bash
pip install requests
```

- A GitHub Personal Access Token (PAT) for authentication. This can be generated from your GitHub account settings under "Developer settings" > "Personal access tokens".

### **1. Creating a New Repository**

**Filename:** **`create_repo.py`**

Automating the creation of a new repository is a breeze with the GitHub API:

```python
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
        "auto_init": True  # Initializes the repo with a README.md
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"Repository {repo_name} created successfully!")
    else:
        print(f"Failed to create the repository. {response.json()['message']}")

create_repo("test-repo")
```

### **2. Committing a File**

**Filename:** **`commit_file.py`**

With our repository in place, let's commit a file to it:

```python
def commit_file(repo_name, file_content="Hello from API!"):
    url = f"{API_URL}/repos/YOUR_GITHUB_USERNAME/{repo_name}/contents/hello.txt"
    data = {
        "message": "Add hello.txt",
        "content": file_content.encode('utf-8').hex()
    }
    response = requests.put(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print("File committed successfully!")
    else:
        print(f"Failed to commit the file. {response.json()['message']}")

commit_file("test-repo")
```

### **3. Retrieving Commit History**

**Filename:** **`fetch_commits.py`**

To keep track of changes, fetching the commit history is essential:

```python
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
```

### **Executing the Scripts**

1. Save the scripts in their respective filenames.
2. Navigate to the directory containing the scripts in your terminal.
3. Execute them in sequence:

```bash
$ python3 create_repo.py
$ python3 commit_file.py
$ python3 fetch_commits.py
```

### **Conclusion**

Python, combined with the GitHub API, offers a potent toolset for automating mundane repository management tasks. This guide provides a foundation, but the possibilities are vast. With these basics, you can expand and tailor the scripts to your specific needs, further enhancing your DevOps workflow.