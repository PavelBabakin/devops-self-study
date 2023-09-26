# Task 1: Install Go on your machine and set up your GOPATH.

## **Setting Up Go on macOS: A Step-by-Step Guide**

Go, often referred to as Golang, is a statically typed, compiled language known for its simplicity and efficiency. Whether you're diving into microservices, DevOps tools, or web development, Go is a fantastic choice. In this guide, we'll walk you through installing Go on macOS and setting up your workspace.

### **1. Installing Go on macOS**

### **Using Homebrew**

For those who have Homebrew installed:

```bash
brew install go
```

### **Manual Installation**

1. Navigate to the official **[Go Downloads page](https://golang.org/dl/)**.
2. Download the macOS distribution.
3. Open the downloaded file and follow the installation prompts.

To verify the installation:

```bash
go version
```

### **2. Understanding GOPATH and Go Modules**

Historically, Go used the GOPATH as a workspace. However, with the introduction of Go modules, dependency management and project setup have become more flexible. While Go modules are now the recommended approach, understanding GOPATH can still be beneficial.

### **Setting Up GOPATH (Optional)**

1. Create a Go workspace:

```bash
mkdir ~/go-workspace
```

1. Set the GOPATH environment variable:

```bash
echo 'export GOPATH=$HOME/go-workspace' >> ~/.zshrc
```

For bash users, replace **`~/.zshrc`** with **`~/.bash_profile`**.

1. Add the **`bin`** directory to your PATH:

```bash
echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.zshrc
```

Reload your shell:

```bash
source ~/.zshrc
```

Or for bash:

```bash
source ~/.bash_profile
```

### **3. Embracing Go Modules**

With Go 1.17 and later, the community is steering towards Go modules. Here's how to use them:

### **Installing Tools (e.g., golint)**

Recent changes in Go have deprecated the global **`go get`** outside a module. To install tools like **`golint`**:

1. Navigate to a temporary directory:

```bash
mkdir ~/temp-golint && cd ~/temp-golint
```

1. Initialize a Go module:

```bash
go mod init temp-golint
```

1. Install **`golint`**:

```bash
go install golang.org/x/lint/golint@latest
```

1. Clean up:

```bash
cd ~ && rm -rf ~/temp-golint
```

### **Conclusion**

Setting up Go on macOS is straightforward, but the evolving nature of the language means developers need to stay updated with best practices. With Go installed and your workspace set up, you're ready to embark on your Go development journey. Whether it's DevOps tools, web applications, or system programs, Go has got you covered!