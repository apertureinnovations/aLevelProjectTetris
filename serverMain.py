import json
import socket
from threading import Thread, ThreadError


class Listener:

    def __init__(self):
        self.host = socket.gethostbyname(socket.gethostname())
        self.running = True
        self.log = []

    def activeConnections(self):
        pass

    def incomingConnection(self):
        pass

    def outgoingConnection(self):
        pass

    def shutdown(self):
        self.running = False

    def dataLog(self):
        f = open("serverLog.txt", "w")
        for i in self.log:
            f.write(i + "\n")
        f.close()
