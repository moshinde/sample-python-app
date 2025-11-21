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
    # Client IP
    client_ip = request.client.host

    # Server hostname
    hostname = socket.gethostname()

    return {
        "status": "success",
        "value": 1234,
        "client_ip": client_ip,
        "server_hostname": hostname
    }