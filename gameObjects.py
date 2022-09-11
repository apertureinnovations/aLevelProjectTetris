from clientMainRework import Board, Tetromino


class TGame(object):
    def __init__(self):
        """ Initialise all game data """
        self.board = Board()
        self.score = 0
        self.held = None
        self.heldFresh = True
        self.clearedCount = 0
        self.currentScore = 0
        self.currentTetromino = Tetromino(self.currentTimeScale, start=self.board.startingCoordinates)
        self.scoreList = [0, 100, 300, 500, 800]
        self.generateNext()
        # score
        # board
        # held
        # etc


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
        self.nextTetromino=Tetromino(self.currentTimeScale, start=self.board.startingCoordinates)
    def keyDown(self):
        print("here")
        while not self.board.collision(self.currentTetromino.shape):
            self.currentTetromino.moveDown()
            self.currentTetromino.translate()
        self.currentTetromino.moveUp()
        self.currentTetromino.translate()
        self.board.setFixed(self.currentTetromino.shape)
        self.currentTetromino = self.nextTetromino
        #self.currentTetromino.translate()
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
