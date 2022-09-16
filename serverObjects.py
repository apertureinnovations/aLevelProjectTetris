class SGame:
    def __init__(self):

        pass

    def request(self, data):

        pass

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

