#!/bin/bash

# Navigate to the app directory
cd the_app/ || echo "Directory not found"

# Pull the latest changes from Git
echo "Pulling the latest changes"
git reset --hard > /dev/null
git pull origin main --force


# sleep 5
# echo "Restarting the server"
# docker-compose down > /dev/null
# docker stop $(docker ps -q) > /dev/null
# docker rm $(docker ps -a -q) > /dev/null


# sleep 5


# docker-compose up --build --remove-orphans -d
# echo "Server is up and running"


# cd frontend/ || echo "Directory not found"


# docker ps
