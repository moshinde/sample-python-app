from fastapi import FastAPI, Request
import socket

app = FastAPI()

@app.get("/")
def root():
    hostname = socket.gethostname()
    return {
        "message": "App deployed using App Service Build",
        "hostname": hostname
    }

@app.get("/api/data")
def get_data(request: Request):
    client_ip = request.client.host
    hostname = socket.gethostname()

    return {
        "status": "success",
        "value": 1234,
        "client_ip": client_ip,
        "server_hostname": hostname
    }

# NEW: For testing Application Gateway path rules
@app.get("/test/appgw")
def test_appgw(request: Request):
    client_ip = request.client.host
    hostname = socket.gethostname()

    return {
        "route": "/test/appgw",
        "message": "Application Gateway path rule working!",
        "client_ip": client_ip,
        "server_hostname": hostname
    }