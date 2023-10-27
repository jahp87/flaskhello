from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/getinstance")
async def list_instance():
    return ['instance1', 'instance2', 'instance3']
