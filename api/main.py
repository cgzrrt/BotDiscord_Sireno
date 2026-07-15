from fastapi import FastAPI
from threading import Thread

app = FastAPI()

@app.get("/")
def home():
    return "Discrod bot ok"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()