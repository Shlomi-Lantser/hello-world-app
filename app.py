from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/hello")
def hello():
    return {"message": "Hello World"}


@app.get("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    port = int(os.getenv("PORT", 9000))
    uvicorn.run("app:app", host="0.0.0.0", port=port)