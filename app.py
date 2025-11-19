from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API deployed successfully!"}

@app.get("/api/data")
def get_data():
    return {"value": 100, "status": "OK"}