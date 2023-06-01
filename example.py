from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Up and running!"}

@app.post("/webhook")
def webhook():
    return {"message": "webhook is working"}

@app.get("/webhook")
def webhook():
    return {"message": "webhook /get is working"}


handler = Mangum(app)
