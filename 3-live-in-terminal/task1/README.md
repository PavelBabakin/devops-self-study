# Task 1: Navigate the file system using commands like cd, ls, pwd, and find.

Hello, dear readers! Today, we're embarking on an exciting journey into the world of the terminal. If you've ever been curious about how to navigate your computer's file system using the command line, you're in the right place. We'll be exploring four fundamental commands: **`cd`**, **`ls`**, **`pwd`**, and **`find`**. Let's dive in!

### 1. **`cd` (Change Directory)**

The **`cd`** command, short for "change directory," is your trusty steed when it comes to moving around the file system. It allows you to switch from one directory to another.

**Usage**:

```bash
cd [directory_name]
```

**Examples**:

- To navigate to your home directory: **`cd ~`** or simply **`cd`**
- To move up one directory level: **`cd ..`**
- To go into a specific directory: **`cd Documents`**

### 2. **`ls` (List)**

Once you're in a directory, you might wonder, "What's in here?" That's where the **`ls`** command comes in. It lists the contents of a directory.

**Usage**:

```bash
ls [options] [directory_name]
```

**Examples**:

- To list files in the current directory: **`ls`**
- To list files with detailed information including file permissions, number of links, owner, group, size, and time of last modification: **`ls -l`**
- To list all files, including hidden ones: **`ls -a`**

### 3. **`pwd` (Print Working Directory)**

Lost in the maze of directories? The **`pwd`** command is your compass. It displays the full pathname of the current working directory.

**Usage**:

```bash
pwd
```

**Example**:

```bash
$ pwd
/Users/yourusername/Documents
```

### 4. **`find` (Find Files)**

The **`find`** command is a powerful tool for searching files and directories. It allows you to locate files based on various criteria such as name, size, type, and more.

**Usage**:

```bash
find [path] [expression]
```

**Examples**:

- To find a file named "example.txt" in the current directory and its subdirectories: **`find . -name "example.txt"`**
- To find all directories named "Documents" starting from the root directory: **`find / -type d -name "Documents"`**
- To find all files larger than 100MB in the **`/home`** directory: **`find /home -type f -size +100M`**

### **Conclusion**

Navigating the file system using the terminal might seem daunting at first, but with these four commands in your toolkit, you'll be zipping around your directories in no time. Practice makes perfect, so fire up your terminal and start exploring! Stay tuned for our next article, where we'll delve deeper into more advanced terminal commands.