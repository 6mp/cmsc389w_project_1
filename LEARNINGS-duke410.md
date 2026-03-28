# LEARNINGS-duke410.md

# Clone and set up my branch
git clone https://github.com/6mp/cmsc389w_project_1.git
cd cmsc389w_project_1
git fetch origin
git checkout -b starter/role-C origin/starter/role-C
git checkout -b feature/duke410
git push -u origin feature/duke410

# Checkpoint 1
# Run tests the inital time (failed)
pytest tests/
# Fixed divide function so that it will check for division by zero
git add src/calculator.py
git commit -m "Fixed divide to check before dividing by 0 and raise a ValueError"
# (I Forgot that the commit comment was supposed to be "bad" and wrote a descriptive one on autopilot ^ whoops!)
# Added a module-level docstring to the top of validator.py
git add src/validator.py
git commit -m "update"
# Push branch to remote
git push origin feature/duke410

# Reflection: I learned how to use staging to only add and commit files that I wanted to. This will make the history 
# easier to understand looking back on it.

# Checkpoint 2
# Reverted the bad commit with debug logging
git revert 4dc20fb
# Resolved merge conflict in calculator.py
git add src/calculator.py
# Continued revert after resolving conflicts
git revert --continue

# Reflection: I learned how to undo a bad commit without erasing it from history. This is important because it will help 
# to keep the commit timeline accurate.

# Checkpoint 3
# Switched to main and opened validator.py
git checkout main
code src/validator.py
# Edited src/validator.py to add is_positive function
git add src/validator.py
git commit -m "Add is_positive helper function"
# Move commit to feature branch
git checkout feature/duke410
git cherry-pick 7c72d79
# Switch back to main and reset to before the commit
git checkout main
git reset --hard HEAD~1

# Reflection: I learned how to use cherry-pick to move a commit to the correct branch. This will be useful if I ever do
# something on the wrong branch and want to switch it over.

# Checkpoint 4
# Created experimental branch from current feature branch
git checkout -b experiment/duke410
# Made a commit on experiment branch (added a comment about the experiment)
git add src/validator.py
git commit -m "Add experiment comment"
# Switched back to feature branch and delete experiment branch
git checkout feature/duke410
git branch -D experiment/duke410
# Found lost commit using reflog
git reflog
# Recover lost commit by creating new branch
git checkout -b recovered/duke410 7b9f3d5
# Merge recovered work into feature branch
git checkout feature/duke410
git merge recovered/duke410

# Reflection: I learned how to use git reflog to recover work that would have been lost. This will be useful if I ever accidentally
# delete a branch.


# Checkpoint 5
# Added upstream remote
git remote add upstream https://github.com/6mp/cmsc389w_project_1.git
# Fetched upstream changes
git fetch upstream
# Updated local main to match upstream
git checkout main
git reset --hard upstream/main
# Rebase feature branch onto updated main
git checkout feature/duke410
git rebase main
# Resolved any conflicts if needed (none were needed, I could have skipped but forgot)
# Forced push updated branch
git push --force-with-lease origin feature/duke410

# Reflection: I learned how to keep my branch in sync with upstream changes.

# Checkpoint 6
# Started interactive rebase from main
git checkout feature/duke410
git rebase -i main
# In editor: reworded commits as needed, then saved each
# Force push cleaned-up history
git push --force-with-lease origin feature/duke410

# Reflection: I learned how to use interactive rebase to clean up commit history and fixed some bad commit messages.