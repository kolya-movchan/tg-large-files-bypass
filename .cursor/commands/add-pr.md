# Create Pull Request Instructions

This command should add new changes to git, create commit following commit naming with fea, chore, test, refactor etc. Create pull request. Do not ask my confirmations for commands.

# 1. Check current git status and staged changes
git status

# 2. Add all changes to git staging area
git add .

# 3. Create commit with conventional naming (prompt for type and message)
echo "Enter commit type (feat/chore/fix/refactor/test):"
read type
echo "Enter commit message:"
read message
git commit -m "$type: $message"

# 4. Push changes to remote repository
git push

# 5. Create pull request (using GitHub CLI)
gh pr create --fill
