import socket
import json

class SGame:
    def __init__(self):
        self.hostName = 0.0.0.0
        self.port = 56365
        self.handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.handler.connect((self.hostName, self.port))
        pass

    def request(self, data):
        self.handler.sendall(data.encode)
        running = True
        while running:
            Data = self.handler.recv(1024)
            if not Data:
                continue
            else:
                running = False
                return json.loads(Data.decode())

    def getCurrentTetrominoState(self):
        return self.request("currentTetrominoState")
        pass

    def getCurrentBoardState(self):
        return self.request("currentBoardState")
        pass

    def getCurrentNextState(self):
        return self.request("currentNextState")
        pass

    def getCurrentHoldState(self):
        return self.request("currentHoldState")
        pass

    def getCurrentSpeed(self):
        return self.request("currentSpeed")
        pass

    def getCurrentScores(self):
        return self.request("currentScores")
        pass

    def getMoveAutomatic(self):
        return self.request("moveAutomatic")
        pass

