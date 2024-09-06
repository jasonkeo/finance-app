cd the_app/
git pull origin main > /dev/null
echo "Pulling the latest changes"
sleep 5
echo "Restarting the server"
docker stop $(docker ps -q) > /dev/null
docker rm $(docker ps -a -q) > /dev/null
sleep 5
docker build -no-cache > /dev/null
docker compose up --remove-orphans > /dev/null
echo "Server is up and running"
cd frontend/
PORT=3000 npm run dev
docker ps
