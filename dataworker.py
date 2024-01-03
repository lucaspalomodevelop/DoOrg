import os
import sys
import DockerComunicator as DockerComunicator


class dataworker:
    def __init__(self):
        self.call_dir = "."
        self.accepted_dockerfiles = [
            "docker-compose.yml",
            "docker-compose.yaml",
            "docker-compose.yml.j2",
            "docker-compose.yaml.j2",
        ]
        self.DockerComunicator = DockerComunicator.DockerComunicator()

    def is_valid_service(self, service):
        service_dir = self.call_dir + "/services/" + service
        for dockerfile in self.accepted_dockerfiles:
            if os.path.isfile(service_dir + "/" + dockerfile):
                return True
        return False

    def get_services(self):
        services = []
        services_dir = self.call_dir + "/services"
        for service in os.listdir(services_dir):
            # print("Checking service " + service)
            if os.path.isdir(services_dir + "/" + service) and self.is_valid_service(
                service
            ):
                services.append(service)
            else:
                print(
                    cli_style.RED
                    + "Service "
                    + services_dir
                    + "/"
                    + service
                    + " is not a valid service"
                    + cli_style.RESET
                )
        return services

    def get_running_services(self):
        services = []
        docker_services = self.DockerComunicator.get_services()
        for service in docker_services:
            services.append(service.name)
        return services
