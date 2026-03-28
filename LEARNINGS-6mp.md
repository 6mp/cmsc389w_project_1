# LEARNINGS-6mp

## Checkpoint 1: Staging Is Not Committing

Commands:
- git checkout starter/role-A
- git checkout -b feature/6mp
- git add tests/test_calculator.py
- git commit -m "fix"
- git add src/calculator.py
- git commit -m "update"

Reflection: The staging area lets you control exactly which changes go into each commit. You can use git add on specific files to create focused, separate commits.

## Checkpoint 2: Undo Without Erasing History

Commands:
- git log --oneline
- git revert 66f6716

Reflection: git revert creates a new commit that undoes a previous commit's changes without removing it from history. This is safer than rewriting history.

## Checkpoint 3: Moving a Commit to the Right Branch

Commands:
- git checkout main
- git add src/validator.py
- git commit -m "Add is_positive helper function"
- git reset --hard HEAD~1
- git checkout feature/6mp
- git cherry-pick 58ab7b4
- git add src/validator.py
- git cherry-pick --continue

Reflection: git cherry-pick copies a specific commit from one branch to another. When conflicts arise, you resolve them manually and continue the operation.

## Checkpoint 4: Recovering Lost Work with Reflog

Commands:
- git checkout -b experiment/6mp
- git add src/calculator.py
- git commit -m "Add experimental comment for future power operation"
- git checkout feature/6mp
- git branch -D experiment/6mp
- git reflog
- git branch recovered/6mp ad40af8
- git merge --no-ff recovered/6mp -m "Merge recovered/6mp into feature/6mp"

Reflection: git reflog tracks every HEAD movement, so even after deleting a branch, the commits aren't truly gone. It can recover lost work.

## Checkpoint 5: Syncing with Upstream

Commands:
- git remote add upstream git@github.com:6mp/cmsc389w_project_1.git
- git fetch upstream
- git checkout main
- git merge --ff-only upstream/main
- git checkout feature/6mp
- git rebase main
- git push --force-with-lease origin feature/6mp

Reflection: Rebasing your feature branch onto the updated main gives you a linear history and surfaces any conflicts early.

## Checkpoint 6: Interactive Rebase to Clean Up History

Commands:
- git log main..HEAD --oneline
- git rebase -i main
- git push --force-with-lease origin feature/6mp

Reflection: Interactive rebase lets you reword messages, squash related commits, drop unnecessary ones, and reorder commits to create a clean history before sharing your work.
