from clientMainRework import Board, Tetromino
import json


class TGame(object):
    def __init__(self):
        """ Initialise all game data """
        self.board = Board()
        self.score = 0
        self.held = None
        self.heldFresh = True
        self.clearedCount = 0
        self.currentScore = 0
        self.scoreMultiplier = 0
        self.nextTetromino = None
        self.currentTetromino = Tetromino(self.currentTimeScale, start=self.board.startingCoordinates)
        self.scoreList = [0, 100, 300, 500, 800]
        self.generateNext()

    def grabTime(self):
        packageTimeJSON = json.dumps(self.currentTimeScale)
        return packageTimeJSON

    def currentBoardState(self):
        packageGameState = {"blockSize": self.currentTetromino.blockSize, "boardFixed": self.board.fixed}
        packageGameStateJSON = json.dumps(packageGameState)
        return packageGameStateJSON

    def currentTetrominoState(self):
        packageStateJSON = json.dumps(self.currentTetromino.state())
        return packageStateJSON

    def currentNextState(self):
        packageStateJSON = json.dumps(self.nextTetromino.shapeState())
        return packageStateJSON

    def currentHoldState(self):
        packageStateJSON = json.dumps(self.held.shapeState())
        return packageStateJSON

    def getScores(self):
        self.scoreMultiplier = self.scoreSys()
        self.clearedCount += self.scoreMultiplier
        self.currentScore += self.scoreList[self.scoreMultiplier]
        packageScore = {"clearCount": self.clearedCount, "currentScore": self.currentScore}
        packageScoreJSON = json.dumps(packageScore)
        return packageScoreJSON

    def scoreSys(self, curScore=0):
        for y in range(self.board.boardSize[1]):
            y += 1
            for x in range(self.board.boardSize[0]):
                x += 1
                if not (x, y) in self.board.fixed:
                    break
            else:
                tempList = []
                for xVal, yVal in self.board.fixed:
                    if yVal < y:
                        tempList.append((xVal, yVal + 1))
                    elif yVal > y:
                        tempList.append((xVal, yVal))
                self.board.fixed = tempList
                curScore += 1

                curScore = self.scoreSys(curScore)

        return curScore

    @property
    def blockSize(self):
        return self.currentTetromino.blockSize

    def keyRight(self):
        self.currentTetromino.moveRight()
        self.currentTetromino.translate()
        if self.board.collisionLeftRight(self.currentTetromino.shape, "right"):
            self.currentTetromino.moveLeft()
            self.currentTetromino.translate()

    def keyLeft(self):
        self.currentTetromino.moveLeft()
        self.currentTetromino.translate()
        if self.board.collisionLeftRight(self.currentTetromino.shape, "left"):
            self.currentTetromino.moveRight()
            self.currentTetromino.translate()

    def keyUp(self):
        self.currentTetromino.rotateTetromino()
        self.currentTetromino.translate()
        if self.board.collision(self.currentTetromino.shape) or self.board.collisionLeftRight(
                self.currentTetromino.shape, "both"):
            self.currentTetromino.horizontalFlip()
            self.currentTetromino.transpose()

    def generateNext(self):
        self.nextTetromino = Tetromino(self.currentTimeScale, start=self.board.startingCoordinates)

    def keyDown(self):
        print("here")
        while not self.board.collision(self.currentTetromino.shape):
            self.currentTetromino.moveDown()
            self.currentTetromino.translate()
        self.currentTetromino.moveUp()
        self.currentTetromino.translate()
        self.board.setFixed(self.currentTetromino.shape)
        self.currentTetromino = self.nextTetromino
        # self.currentTetromino.translate()
        self.generateNext()
        self.heldFresh = True

        if self.board.collision(self.currentTetromino.shape):
            return False
        return True

    def keyHold(self):
        if self.heldFresh:
            if self.held is None:
                self.held = self.currentTetromino
                self.held.xMod, self.held.yMod = self.board.startingCoordinates
                self.currentTetromino = self.nextTetromino
                self.heldFresh = False
                self.generateNext()

            else:

                tempValue = self.currentTetromino
                self.currentTetromino = self.held
                self.held = tempValue
                self.held.xMod, self.held.yMod = self.board.startingCoordinates
                self.currentTetromino.translate()
                self.heldFresh = False
                if self.board.collision(self.currentTetromino.shape):
                    return False
        return True

    def moveAutomatic(self):
        self.currentTetromino.moveDown()
        self.currentTetromino.translate()
        if self.board.collision(self.currentTetromino.shape):
            self.currentTetromino.moveUp()
            self.currentTetromino.translate()
            self.board.setFixed(self.currentTetromino.shape)
            self.currentTetromino = self.nextTetromino
            self.currentTetromino.translate()
            self.generateNext()
            self.heldFresh = True
            if self.board.collision(self.currentTetromino.shape):
                return False
        return True

    @property
    def currentTimeScale(self):
        if self.clearedCount == 0:
            return 1
        else:
            return 1 + self.clearedCount / 25
