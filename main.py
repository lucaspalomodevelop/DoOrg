#!/bin/python3

import os
import DockerComunicator as DockerComunicator


VERSION = "0.0.1"
call_dir = ""

DockerComunicator = DockerComunicator.DockerComunicator()


class style:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


accepted_dockerfiles = [
    "docker-compose.yml",
    "docker-compose.yaml",
    "docker-compose.yml.j2",
    "docker-compose.yaml.j2",
]


def is_valid_service(service):
    service_dir = call_dir + "/services/" + service
    for dockerfile in accepted_dockerfiles:
        if os.path.isfile(service_dir + "/" + dockerfile):
            return True
    return False


def get_services():
    services = []
    services_dir = call_dir + "/services"
    for service in os.listdir(services_dir):
        # print("Checking service " + service)
        if os.path.isdir(services_dir + "/" + service) and is_valid_service(service):
            services.append(service)
        else:
            print(
                style.RED
                + "Service "
                + services_dir
                + "/"
                + service
                + " is not a valid service"
                + style.RESET
            )
    return services


if __name__ == "__main__":
    call_dir = os.getcwd()
    print("DoOrg v" + VERSION)
    print("call dir: " + call_dir)
    services = get_services()
    print("Services:")
    for service in services:
        color = (
            style.GREEN if DockerComunicator.is_service_running(service) else style.RED
        )
        print(color + " - " + service + style.RESET)

    print("Docker services:")
    docker_services = DockerComunicator.get_services()
    for service in docker_services:
        print(" - " + service.name)
