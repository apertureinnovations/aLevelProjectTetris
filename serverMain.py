import json
import socket
import threading
from gameObjects import TGame


class Listener:
    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.running = True
        self.log = []
        self.port = 56365
        self.Data = None
        self.funNameList = []
        self.handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.handler.bind((self.hostName, self.port))

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def incomingConnection(self):
        while True:
            self.Data = self.handler.recv(1024)
            if not self.Data:
                continue
            else:
                break

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def outgoingConnection(self, clientName, dataToSend):
        pass

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def shutdown(self):
        self.running = False

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def dataLog(self):
        f = open("serverLog.txt", "w")
        for i in self.log:
            f.write(i + "\n")
        f.close()
