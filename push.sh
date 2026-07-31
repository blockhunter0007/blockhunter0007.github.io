#!/bin/bash
read -p "Enter commit message: " commit_message
if [ -z "$commit_message" ]; then
    echo "Commit message cannot be empty. Aborting."
    exit 1
fi
git add .
git commit -m "$commit_message"
git push origin main
sleep 5