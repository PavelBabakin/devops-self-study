# Task 7: Create a Go utility to backup and compress (tar) a directory.

## **Creating a Directory Backup Utility with Go**

In the world of DevOps, ensuring that data is backed up and can be easily restored is paramount. While there are many tools available for this purpose, sometimes you might need a custom solution tailored to your specific needs. In this tutorial, we'll explore how to use Go (or Golang) to create a utility that backs up and compresses a directory.

### **Why Go for Directory Backup?**

Go offers a rich standard library that provides out-of-the-box support for many common tasks, including file handling, compression, and archiving. Its efficient runtime and straightforward syntax make it an excellent choice for building utilities and CLI tools.

### **Building the Directory Backup Utility in Go**

1. **The Core Function - `tarDirectory`**:
    
    The heart of our utility is the **`tarDirectory`** function. This function takes a source directory and a target file path as arguments. It then compresses the directory into a tarball at the specified target location.
    
    ```go
    func tarDirectory(source, target string) error {
        // ... (code for compression and archiving)
    }
    ```
    
2. **Walking Through the Directory**:
    
    Go's **`filepath.Walk`** function allows us to traverse through every file and sub-directory of the given directory. For each file, we add its details to the tarball and copy its content.
    
3. **Compression with Gzip**:
    
    To reduce the size of our backup, we use Go's **`gzip`** package to compress the tarball.
    
4. **Bringing It All Together**:
    
    The **`main`** function of our utility sets the source directory and target tarball path, then calls the **`tarDirectory`** function to perform the backup.
    
    ```go
    func main() {
        sourceDir := "./sampledir"
        targetTar := "./backup.tar.gz"
    
        err := tarDirectory(sourceDir, targetTar)
        if err != nil {
            fmt.Println("Error:", err)
            return
        }
    
        fmt.Printf("Directory %s has been compressed to %s\n", sourceDir, targetTar)
    }
    ```
    
5. **Running the Utility**:
    
    To use the utility, navigate to its directory in the terminal and execute:
    
    ```bash
    go run tarbackup.go
    ```
    
    The utility will then compress the specified directory into a tarball.
    

### **Conclusion**

With just a few lines of Go code, we've crafted a robust directory backup utility. This exercise not only showcases Go's capabilities in file handling and compression but also demonstrates its potential as a go-to language for building utilities and tools. As you continue your journey with Go, you'll discover its vast potential in various domains, from system utilities to web applications and beyond.