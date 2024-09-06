#!/bin/bash

# Navigate to the app directory
cd the_app/ || exit

# Pull the latest changes from Git
echo "Pulling the latest changes"
git pull origin main > /dev/null

# # Pause for 5 seconds (optional)
# sleep 5

# # Restart the server
# echo "Restarting the server"
# docker stop $(docker ps -q) > /dev/null
# docker rm $(docker ps -a -q) > /dev/null

# # Pause for 5 seconds (optional)
# sleep 5

# # Rebuild and bring up containers
# docker-compose up --build --remove-orphans -d > /dev/null
# echo "Server is up and running"

# # Navigate to the frontend directory and manually run npm dev
# cd frontend/ || exit
# PORT=3000 npm run dev

# # Show running containers
# docker ps
