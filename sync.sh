#!/bin/bash
echo "Pulling the latest changes"
git reset --hard > /dev/null
git pull origin main --force
