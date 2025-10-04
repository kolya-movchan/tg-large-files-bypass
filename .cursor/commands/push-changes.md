# Push Pull Request Instructions

This command should add new changes to git, create commit following commit naming with fea, chore, test, refactor etc. Create pull request. Do not ask my confirmations for commands. Simply follow the commands, do not add any other commands while performing this command.

# 1. Add all changes to git staging area
git add .

# 2. Create commit with conventional naming (prompt for type and message)
echo "Enter commit type (feat/chore/fix/refactor/test):"
read type
echo "Enter commit message:"
read message
git commit -m "$type: $message"

# 3. Push changes to remote repository
git push
