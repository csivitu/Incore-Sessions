# Git & GitHub
_Notes for CSI VIT incore-session on Git, GitHub and version control conducted on 23.08.2023._

### What is Git?

- Version Control Manager
- Works like a video game with checkpoints.
- In code, we need commits which act as checkpoints.

### What is GitHub?

A hosting platform for collaborating on projects.

### Open Source

- Projects for which the code is made publicly available.
- VS Code is an open source project by Microsoft.
- People can contribute by improving code and also by raising issues.

### Branches

- When a new project is started, we start with one branch, typically called “main”.
- If a new developer wants to work on a feature, they can create a new branch from main branch.
- Branches are useful when multiple developers are working on the same issue or file. Good companies tend to work with multiple branches to avoid conflicts.
- Developers working on a project work issue-by-issue. An issue can be a feature or a bug fix.

### Merging Changes

When a developer has finished making changes in a new branch, they can make a Pull Request (PR) to merge the code in their branch with the master branch.

In a scenario where a developer tries to merge a branch into master branch that is not updated with the latest changes from master branch, the developer needs to create a PR and then there will be a Merge Conflict which needs to be resolved.

**Example:** dev1 is working on the signup feature and makes commits 1,2,3. Then dev2 creates a branch from the master branch to work on a button feature. Then dev1 makes a new commit 4 to the master branch. Now when dev2 creates a PR to merge their branch to master branch, a Merge Conflict arises. This can be resolved by dev1 by adding commit 4 to the final changes.

### Master or Main?

Earlier, git used “master” for the first branch created in new projects. Now it has been updated to “main”. All projects initialized in git have the default branch as “main”.

### Staging Area

Whenever we make any changes in a project, we first add the changes to the “staging area”. Then when we commit changes, the changes in the staging area are committed to the current branch.

### Working with Git in VS Code

- If working on a GitHub project, we first clone the repository into a folder on our machine. Then after making some necessary changes, we can add our modified files to the staging area. Once a feature or bugfix is finished, we can commit all the changes in the staging area. Finally, all commits made on the local machine need to be pushed to the origin (repository on GitHub) by making a Pull Request (PR).
- Before making any changes, we can create a new branch to work on. This should be done if you are working on some major changes or if multiple people are working on the same file or issue.
> M - modified file<br>
U - untracked file

### Best Practice

- Before working on a repository, clone it and create a new branch to work on 1 specific feature.
- Make commits only to your branch.
- When the feature is finished, make a Pull Request to merge your branch to the main branch.
- The project organizer will then review your changes and merge them if they approve.

### What is Forking?

- When we fork a repository, a copy of the repository is made on your profile. Repositories for which we don’t have direct access or permission to work on, have to be first forked.
- The entire process of cloning, adding changes to staging area, committing changes and merging to main branch has to be first done on the forked repository.
- Then once the feature is added to the forked repository, we create a Pull Request to merge our branch with the main project branch.
- If the project manager approves of our feature, they will merge the branch.
- Both individual developers and organizations can fork repositories to work on. The advantage of this is that developers can continue working on discontinued projects i.e. projects with no active contributors.
- You can also fork a forked repository.

### Git Commands



`git init`

- This command is used to start / initialize a new project with git.

`git add file_name.extension`

- This command is used to add a changed file to the staging area.
- Example: git add index.html

`git add .`

- This command adds all changed files to the staging area.

`git commit -m "commit_message_here"`

- This command commits the changes in the staging area.
- Example: git commit -m “feat: sign up page added”

`git remote add origin repository_url`

- This command tells Git where the commits need to be pulled when a PR is created.

- Origin is the repository on the cloud from where changes are fetched and pushed.

`git clone repository_url`

- This is used to clone a repository from cloud (such as GitHub) to the local machine.

`git checkout -b branch_name`

- This is used to move to another branch. If it doesn’t exist, a new branch is created.

- Example: git checkout -b button

`git branch`

- This is used to check the current branch.

`git fetch`

- This is used to fetch all the updated changes from origin.

`git pull origin main`

- This will update the main branch on your local machine with changes from origin.

`git pull origin branch_name`

- This will update a specific branch on your local machine with changes from that branch present on the origin.

`git log`

- Shows history of all changes made to repository.
