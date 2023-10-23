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