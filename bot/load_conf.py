import json

with open("config.json", mode="r", encoding="utf-8") as cnfg:
    data = json.loads(cnfg.read())

TOKEN = data.get("Token")
HOST = data.get("HOST")
USER = data.get("USER")
PORT = data.get("PORT")
DB = data.get("DB")
PASSW = data.get("PASSW")
