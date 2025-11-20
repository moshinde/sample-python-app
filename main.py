from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "App deployed using App Service Build"}

@app.get("/api/data")
def get_data():
    return {"status": "success", "value": 1234}