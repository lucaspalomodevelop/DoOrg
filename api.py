from typing import Union
import uvicorn
from fastapi import FastAPI
import dataworker
import json

app = FastAPI()
dataworker = dataworker.dataworker()


class api:
    def __init__(self):
        self._commands = {}

    def run(self):
        uvicorn.run(app, host="0.0.0.0", port=8000)

    @app.get("/api/v1")
    def read_root():
        return {"Hello": "World"}

    @app.get("/api/v1/services")
    def get_services():
        services = {}
        services["exists"] = []
        services["running"] = []
        for service in dataworker.get_services():
            services["exists"].append(service)
        for service in dataworker.get_running_services():
            services["running"].append(service)
        return services

    @app.get("/api/v1/service/{service_name}/start")
    def start_service(service_name: str):
        if dataworker.is_valid_service(service_name):
            if dataworker.DockerComunicator.is_service_running(service_name):
                return {"status": "Service already running"}
            else:
                dataworker.DockerComunicator.start_service(service_name)
                return {"status": "Service started"}
        else:
            return {"status": "Service not found"}

    @app.get("/api/v1/service/{service_name}/stop")
    def stop_service(service_name: str):
        if dataworker.is_valid_service(service_name):
            if dataworker.DockerComunicator.is_service_running(service_name):
                dataworker.DockerComunicator.stop_service(service_name)
                return {"status": "Service stopped"}
            else:
                return {"status": "Service already stopped"}
        else:
            return {"status": "Service not found"}
