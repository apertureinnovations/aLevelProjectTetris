import socket
import json
import threading


class SGame:
    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def __init__(self):
        self.hostName = "0.0.0.0"
        self.port = 56365
        self.handler = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.handler.connect((self.hostName, self.port))
        self.currentLine = None
        pass

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def request(self, data):
        self.handler.sendall(data.encode)
        while True:
            Data = self.handler.recv(1024)
            if not Data:
                continue
            else:
                temp = json.loads(Data.decode())
                if temp[0] == "confirmed":
                    return temp
                else:
                    continue

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def listener(self):
        threading.Thread(target=self.listenerContainer, args="")
        pass

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def listenerContainer(self):
        while True:
            Data = self.handler.recv(1024)
            if not Data:
                continue
            else:
                temp = json.loads(Data.decode())
                if temp[0] != "confirmed":
                    self.currentLine = temp

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def getCurrentTetrominoState(self):
        data = self.request("currentTetrominoState")
        return data[1]

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def getCurrentBoardState(self):
        data = self.request("currentBoardState")
        return data[1]

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def getCurrentNextState(self):
        data = self.request("currentNextState")
        return data[1]

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def getCurrentHoldState(self):
        data = self.request("currentHoldState")
        return data[1]

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def getCurrentSpeed(self):
        data = self.request("currentSpeed")
        return data[1]

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def getCurrentScores(self):
        data = self.request("currentScores")
        return data[1]

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def getMoveAutomatic(self):
        data = self.request("moveAutomatic")
        return data[1]

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def keyRight(self):
        data = self.request("keyRight")
        return data[1]

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def keyLeft(self):
        data = self.request("keyLeft")
        return data[1]

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def keyUp(self):
        data = self.request("keyUp")
        return data[1]

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def keyDown(self):
        data = self.request("keyDown")
        return data[1]

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def keySpace(self):
        return self.request("keySpace")
        pass

    # FunName (  )
    # Desc (  )
    # Author ( Jake )
    # Parameters (  )
    # Return Values ( )
    # Created ( 29 / 09 / 22 )
    def keyHold(self):
        return self.request("keyHold")
        pass
