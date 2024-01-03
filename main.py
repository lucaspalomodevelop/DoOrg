#!/bin/python3

import os
import sys
import DockerComunicator as DockerComunicator
import cli as cli
import api as api


VERSION = "0.0.1"
call_dir = ""

cli = cli.cli()
api = api.api()


if __name__ == "__main__":
    if sys.argv[1] == "cli":
        cli.run()
    if sys.argv[1] == "api":
        api.run()
