# Task 21: Practice undoing the last commit using git reset.

In the journey of code development, mistakes are inevitable. Whether it's a typo, a bug, or a misconfiguration, the ability to undo changes is crucial. Git, with its powerful command **`git reset`**, provides developers with a safety net, allowing them to undo their last commit and navigate through potential missteps. This article will guide you through the process of undoing the last commit using **`git reset`**, ensuring you can correct course when necessary.

---

### Understanding **`git reset`**

**`git reset`** is a command that allows you to:

- **Undo Changes**: Revert changes made in the working directory, staging area, or commit history.
- **Navigate History**: Move the HEAD and current branch pointer to a specified commit.
- **Modify Staging Area**: Unstage changes while retaining modifications in the working directory.

---

### Step-by-Step Guide to Undoing the Last Commit

### **Step 1: Viewing the Log**

- Before resetting, view your commit history to identify where to navigate:

```bash
git log --oneline
```

### **Step 2: Soft Reset**

- To undo the last commit but keep the changes in the staging area, use a soft reset:

```bash
git reset --soft HEAD~1
```

Here, **`HEAD~1`** indicates moving one commit back from the current position.

### **Step 3: Mixed Reset (Default)**

- To undo the last commit and unstage the changes (keeping them in the working directory), use a mixed reset:

```bash
git reset HEAD~1
```

Or,

```bash
git reset --mixed HEAD~1
```

### **Step 4: Hard Reset**

- To undo the last commit and discard all changes, use a hard reset:

```bash
git reset --hard HEAD~1
```

### **Step 5: Pushing Changes to Remote Repository**

- If you've already pushed your changes to a remote repository, you'll need to force push after the reset:

```bash
git push origin [Branch-Name] --force
```

Replace **`[Branch-Name]`** with the name of your branch.

---

### Best Practices for Using **`git reset`**

- **Caution with Hard Reset**: Be cautious when using **`-hard`** as it discards all changes, and they cannot be recovered.
- **Avoid Force Pushing on Shared Branches**: Be mindful when force-pushing to shared branches to prevent disrupting others' work.
- **Backup**: Consider creating a backup branch before performing a reset to preserve changes.
- **Use Descriptive Commit Messages**: Ensure commit messages are descriptive to make navigation through the log easier.

---

### Conclusion

**`git reset`** provides developers with a powerful tool to undo changes and navigate through their commit history, offering a safety net for mistakes and a means to refine their development process. By understanding and utilizing the different modes of **`git reset`**, you can manage your project with confidence, ensuring that you can always correct course when necessary.

In the upcoming articles, we will explore more aspects of Git, continuing to build your expertise and capability in managing and contributing to collaborative development projects.

---

**Next Task Preview**: In the next article, we will explore recovering a deleted branch using **`git reflog`** and **`git checkout`**, ensuring you can retrieve lost data and navigate through your Git history effectively.