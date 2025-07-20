curl -X POST http://localhost:8000/api/login/ -H "Content-Type: application/json" -d "{\"email\":\"engebaprospere@gmail.com\", \"password\":\"prospere123\"}"

python app/scripts/create_deputes.py
docker exec -it backend python app/scripts/seed_commissions.py

