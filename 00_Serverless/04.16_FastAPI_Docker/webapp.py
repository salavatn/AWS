from fastapi import FastAPI

app = FastAPI()

@app.get("/api/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/{name}")
async def read_item(name: str):
    return {"Hello": name}

