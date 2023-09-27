# Task 20: Use Go to interact with the GitHub API: create a repository, commit a file, and fetch commit history.

### **Interacting with the GitHub API using Go**

In the world of DevOps, automation is key. Whether it's automating deployment pipelines, infrastructure provisioning, or even simple tasks like creating repositories and committing files, automation can save a lot of time and reduce human errors. In this article, we'll explore how to use Go to interact with the GitHub API, allowing us to automate tasks like creating repositories, committing files, and fetching commit histories.

### **Setting Up**

Before we dive into the code, ensure you have:

1. Go installed on your machine.
2. A GitHub account.
3. A **[personal access token](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)** from GitHub with the necessary permissions.

### **The Go Program**

Our Go program will perform three main tasks:

1. Create a new GitHub repository.
2. Commit a file to the newly created repository.
3. Fetch the commit history of the repository.

Here's the complete code:

```go
package main

import (
	"context"
	"fmt"

	"github.com/google/go-github/v38/github"
	"golang.org/x/oauth2"
)

var ctx = context.Background()

func createRepo(client *github.Client, repoName string) (*github.Repository, error) {
	repo := &github.Repository{Name: github.String(repoName)}
	r, _, err := client.Repositories.Create(ctx, "", repo)
	return r, err
}

func commitFile(client *github.Client, owner, repo, path, message, content string) error {
	opts := &github.RepositoryContentFileOptions{
		Message: github.String(message),
		Content: []byte(content),
	}
	_, _, err := client.Repositories.CreateFile(ctx, owner, repo, path, opts)
	return err
}

func fetchCommitHistory(client *github.Client, owner, repo string) ([]*github.RepositoryCommit, error) {
	commits, _, err := client.Repositories.ListCommits(ctx, owner, repo, nil)
	return commits, err
}

func main() {
	ts := oauth2.StaticTokenSource(
		&oauth2.Token{AccessToken: "YOUR_PERSONAL_ACCESS_TOKEN"},
	)
	tc := oauth2.NewClient(ctx, ts)

	client := github.NewClient(tc)

	// Create a new repo
	repo, err := createRepo(client, "TestRepo")
	if err != nil {
		panic(err)
	}
	fmt.Println("Repository created:", *repo.Name)

	// Commit a file
	err = commitFile(client, "YourGitHubUsername", "TestRepo", "test.txt", "Initial commit", "Hello, DevOps!")
	if err != nil {
		panic(err)
	}
	fmt.Println("File committed to repository.")

	// Fetch commit history
	commits, err := fetchCommitHistory(client, "YourGitHubUsername", "TestRepo")
	if err != nil {
		panic(err)
	}
	fmt.Println("Commit History:")
	for _, commit := range commits {
		fmt.Println(*commit.SHA, *commit.Commit.Message)
	}
}
```

### **Understanding the Code**

1. **Authentication**: We use the **`oauth2`** package to authenticate our requests using the personal access token.
2. **Creating a Repository**: The **`createRepo`** function creates a new repository using the **`Repositories.Create`** method.
3. **Committing a File**: The **`commitFile`** function commits a new file to the specified repository using the **`Repositories.CreateFile`** method.
4. **Fetching Commit History**: The **`fetchCommitHistory`** function fetches the commit history of a specified repository using the **`Repositories.ListCommits`** method.

### **Running the Program**

Save the code in a file named **`github_operations.go`**. To execute the program:

```bash
go run github_operations.go
```

Ensure you replace placeholders like **`"YOUR_PERSONAL_ACCESS_TOKEN"`** with your actual GitHub personal access token and **`"YourGitHubUsername"`** with your GitHub username.

### **Conclusion**

With just a few lines of Go code, we've automated some common tasks on GitHub. This is just the tip of the iceberg; the GitHub API offers a plethora of functionalities that can be leveraged to automate almost any task on GitHub. As you delve deeper into DevOps, consider how tools like this can be integrated into larger automation pipelines, making your workflows smoother and more efficient.