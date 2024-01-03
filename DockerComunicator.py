import docker


class DockerComunicator:
    def __init__(self):
        self.docker_client = docker.from_env()

    def get_services(self):
        return self.docker_client.containers.list()

    def get_service(self, service_name):
        return self.docker_client.containers.get(service_name)

    def is_service_running(self, service_name: str):
        try:
            service = self.get_service(service_name)
            return service.status == "running"
        except docker.errors.NotFound:
            return False

    def start_service(self, service_name: str):
        service = self.get_service(service_name)
        service.start()

    def stop_service(self, service_name: str):
        service = self.get_service(service_name)
        service.stop()
