#!/bin/bash

# Navigate to the app directory
cd the_app/ || echo "Directory not found"

# Pull the latest changes from Git
echo "Pulling the latest changes"
git reset --hard > /dev/null
git pull origin main --force

# Pause for 5 seconds (optional)
sleep 5

# Restart the server
echo "Restarting the server"
docker-compose down > /dev/null
docker stop $(docker ps -q) > /dev/null
docker rm $(docker ps -a -q) > /dev/null

# Pause for 5 seconds (optional)
sleep 5

# Rebuild and bring up containers
docker-compose up --build --remove-orphans -d
echo "Server is up and running"

# Navigate to the frontend directory and manually run npm dev
cd frontend/ || echo "Directory not found"


# Show running containers
docker ps
