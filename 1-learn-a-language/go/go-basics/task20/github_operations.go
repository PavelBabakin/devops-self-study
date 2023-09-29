// github_operations.go

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
