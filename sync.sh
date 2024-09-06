cd the_app/
git pull origin main
sleep 5
echo "Restarting the server"
docker compose down > /dev/null
sleep 5
docker compose up --build --remove-orphans > /dev/null
echo "Server is up and running"
docker ps
