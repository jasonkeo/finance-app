cd the_app/
git pull origin main
docker compose down
docker compose up --build --remove-orphans -d
docker ps
echo "Synced and restarted the server"