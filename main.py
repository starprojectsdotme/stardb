# Importing libraries
import socketserver
import threading
import time

import colorama
from colorama import fore

# Initializing Colorama
colorama.init()

# Initializing settings
settings = ({
    'PORT': 9291, # Server port
    'MAX_CONNECTION': 5, # Maximum connection to the database server.
    'WAIT_TIME': 1, # Times to wait for each client. Higher number will not use as much server resource as lower number, but the times client will have to wait will be larger.
})

#
# DO NOT EDIT ANY OF THE VALUES BELOW AS IT MAY BREAK THE ENTIRE PROGRAM.
#   

# Configuration
connected = 0 # Numbers of users connected to the database server. Do not change this default value as it may breaks the database.
connected_ip = []

