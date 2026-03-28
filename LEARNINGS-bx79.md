# Learnings for Betty Au

## Starting

- git switch starter/role-b
- git switch -c feature/bx79

## Checkpoint 1

- git add src/calculator.py
- git commit -m "fix"
- git add src/validator.py
- git commit -m "
- git push origin feature/bx79

Here I learned how to stage and commit changes to my branch. This is important because these are basic git commands and is what allows for coordinating groupwork. 

## Checkpoint 2

- git log --oneline
- git revert b19f233
- git commit -m "remove excessive debug logging"

Here I learned how to undo the changes of a past commit which is important for fixing bugs.

## Checkpoint 3

- git switch main
- git add src/validator.py
- git commit "Add is_positive helper function"
- git log --oneline
- git reset --hard f1deb16
- git switch feature/bx79
- git cherry-pick 45016fb
- git add src/validator.py
- git cherry-pick --continue
- git log --oneline
- git switch main
- git log --oneline

Here I learned how to move a commit from one branch to another, which is helpful for making sure that edits are made where they need to be, to maintain efficient organization.

## Checkpoint 4

- git switch feature/bx79
- git switch -c experiment/bx79
- git add src/validator
- git commit -m "added a comment to validator"
- git switch feature bx/79
- git branch -D experiment/bx79
- git reflog
- git switch -c recovered/bx79 bae8475
- git switch feature/bx79
- git merge recovered/bx79

Here I learned how to rebase my feature branch

## Checkpoint 5

- git remote add upstream https://github.com/6mp/git_project_1.git 
- git fetch upstream
- git switch main
- git merge upstream/main
- git switch feature/bx79
- git rebase main
- git push --force-with-lease origin feature/bx79

Here I learned how to perform rebasing which allows for linearizing history and helping it be more readable.

## Checkpoint 6

- git log main..HEAD --oneline
- git rebase -i HEAD~5
- git push --force-with-lease

Here I learned how to use interactive rebasing to edit commit history, allowing me to make it more legible.

## Checkpoint 7

Here I learned about how to make pull requests and how to interact with other people's pull requests which is needed to coordinate group work.