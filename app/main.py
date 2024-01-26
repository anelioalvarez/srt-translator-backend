from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return "Service is working"
