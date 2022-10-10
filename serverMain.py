import json
import socket
import threading


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

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def activeConnections(self):
        pass

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def incomingConnection(self):
        pass

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def outgoingConnection(self):
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
