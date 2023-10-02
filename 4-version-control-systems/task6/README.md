# Task 6: Make changes in this new branch and commit them.

In our ongoing journey through the world of Git, we've established a foundational understanding of creating branches and switching between them. Now, let’s delve into making changes within a new branch and committing them, thereby encapsulating our modifications safely without affecting the main line of development.

---

### The Power of Branching in Development

Branching allows developers to work on different features or bugs in isolation, safeguarding the main codebase from potential disruptive changes. By making and committing changes in a separate branch, developers can:

- **Work Concurrently**: Multiple features or fixes can be developed in parallel without conflicting.
- **Test Safely**: Changes can be tested without risking the stability of the main codebase.
- **Review Code**: Before merging, code can be reviewed to ensure it adheres to quality and functionality standards.

---

### Step-by-Step Guide to Making and Committing Changes in a New Branch

### **Step 1: Ensure You Are in the Right Branch**

Before making changes, confirm you are in the correct branch using:

```bash
git branch
```

### **Step 2: Making Changes to the Code**

Modify existing files or create new ones as per the feature or fix you are working on. For instance, let’s modify a hypothetical **`README.md`** file:

```bash
echo "New Feature Description" >> README.md
```

### **Step 3: Viewing and Staging Changes**

Use **`git status`** to view the changes and **`git add`** to stage them:

```bash
git status
git add README.md
```

### **Step 4: Committing Changes in the New Branch**

Commit the changes with a meaningful message using **`git commit`**:

```bash
git commit -m "Add description for the new feature in README"
```

### **Step 5: Viewing the Commit History**

Ensure your changes have been committed by viewing the commit history:

```bash
git log
```

---

### Importance of Meaningful Commits in a Branch

- **Clarity**: Clear commits provide insight into the development and changes of a feature or fix, aiding future troubleshooting or enhancement efforts.
- **Revertible**: In case of issues, developers can easily revert to a previous commit without affecting the entire feature development.
- **Documented History**: Maintains a documented history of the progression of the feature or fix, useful for onboarding new developers or reviewing the project evolution.

---

### Conclusion

Making and committing changes in a separate branch is a pivotal practice in collaborative development environments, ensuring that the main codebase remains stable while new features or fixes are developed and tested. This practice enhances team collaboration, parallel development, and ensures that the main codebase is shielded from experimental or work-in-progress code.

In the upcoming articles, we will explore merging these changes back into the main branch and managing potential merge conflicts that may arise during the process.

---

**Next Task Preview**: In the next article, we will delve into the process of merging our feature branch back into the main branch, exploring the **`git merge`** command and understanding how to manage and resolve merge conflicts.