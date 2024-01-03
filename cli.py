import os
import dataworker

VERSION = "0.0.1"
call_dir = ""


class cli_style:
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


class cli:
    def __init__(self):
        self.call_dir = "."
        self.dataworker = dataworker.dataworker()

    def run(self):
        self.call_dir = os.getcwd()
        print("DoOrg v" + VERSION)
        print("call dir: " + self.call_dir)
        services = self.dataworker.get_services()
        print("Services:")
        for service in services:
            color = (
                cli_style.GREEN
                if self.dataworker.DockerComunicator.is_service_running(service)
                else cli_style.RED
            )
            print(color + " - " + service + cli_style.RESET)

        print("Docker services:")
        docker_services = self.dataworker.DockerComunicator.get_services()
        for service in docker_services:
            print(" - " + service.name)
