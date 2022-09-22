from clientMainRework import Board, Tetromino
import json


class TGame(object):

    # FunName ( Init - Startup Function )
    # Desc ( This function gets all the base parameters needed for the tetris game to run and sets up variables
    # that functions later down the line will use.)
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none )
    # Created ( 22 / 09 / 22 )
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
        self.currentTimeScale = 1
        self.currentTetromino = Tetromino(self.currentTimeScale, start=self.board.startingCoordinates)
        self.scoreList = [0, 100, 300, 500, 800]
        self.generateNext()

    # FunName ( Fetch Speed Function )
    # Desc ( fetches the current timescale of the tetris game )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( Current Speed )
    # Created ( 22 / 09 / 22 )
    def grabTime(self):
        packageTimeJSON = json.dumps(self.currentTimeScale)
        return packageTimeJSON

    # FunName ( Fetch Board State Function )
    # Desc ( This function fetches the current board state of the tetris game )
    # Author ( Jake )
    # Parameters ( none)
    # Return Values ( Current Board State )
    # Created ( 22 / 09 / 22 )
    def currentBoardState(self):
        packageGameState = {"blockSize": self.currentTetromino.blockSize, "boardFixed": self.board.fixed}
        packageGameStateJSON = json.dumps(packageGameState)
        return packageGameStateJSON

    # FunName ( Fetch Current Tetronimo Object State Function )
    # Desc ( This function fetches the current tetronimo object state )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( Current Tetronimo state )
    # Created ( 22 / 09 / 22 )
    def currentTetrominoState(self):
        packageStateJSON = json.dumps(self.currentTetromino.state())
        return packageStateJSON

    # FunName ( Fetch Next Tetronimo Object State Function)
    # Desc ( This function fetches the next tetronimo object state )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( Next Tetronimo state )
    # Created ( 22 / 09 / 22 )
    def currentNextState(self):
        packageStateJSON = json.dumps(self.nextTetromino.shapeState())
        return packageStateJSON

    # FunName ( Fetch Held Tetronimo Object State Function )
    # Desc ( This function fetches the current held tetronimo object state )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( Held Tetronimo state )
    # Created ( 22 / 09 / 22 )
    def currentHoldState(self):
        packageStateJSON = json.dumps(self.held.shapeState())
        return packageStateJSON

    # FunName ( Score Fetching Function )
    # Desc ( This function fetches the scores from another function and returns the relevant data. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( Packaged Score Data )
    # Created ( 22 / 09 / 22 )
    def getScores(self):
        self.scoreMultiplier = self.scoreSys()
        self.clearedCount += self.scoreMultiplier
        self.currentScore += self.scoreList[self.scoreMultiplier]
        packageScore = {"clearCount": self.clearedCount, "currentScore": self.currentScore}
        packageScoreJSON = json.dumps(packageScore)
        return packageScoreJSON

    # FunName ( Score System Function )
    # Desc ( This function calculates the score using a recursive algorithm to check what degree of score needs to be added. )
    # Author ( Jake )
    # Parameters ( itself - current score )
    # Return Values ( current score )
    # Created ( 22 / 09 / 22 )
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

    # FunName ( Returning Block Size Function )
    # Desc ( This function behaves as a variable, returning the size of a block that the tetronimos are made of.)
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( block size )
    # Created ( 22 / 09 / 22 )
    @property
    def blockSize(self):
        return self.currentTetromino.blockSize

    # FunName ( Move Right Function )
    # Desc ( Moves an object right when the key is pressed. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none )
    # Created ( 22 / 09 / 22 )
    def keyRight(self):
        self.currentTetromino.moveRight()
        self.currentTetromino.translate()
        if self.board.collisionLeftRight(self.currentTetromino.shape, "right"):
            self.currentTetromino.moveLeft()
            self.currentTetromino.translate()

    # FunName ( Move Left Function )
    # Desc ( Moves an object left when the key is pressed. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none )
    # Created ( 22 / 09 / 22 )
    def keyLeft(self):
        self.currentTetromino.moveLeft()
        self.currentTetromino.translate()
        if self.board.collisionLeftRight(self.currentTetromino.shape, "left"):
            self.currentTetromino.moveRight()
            self.currentTetromino.translate()

    # FunName ( Rotate Tetronimo Function )
    # Desc ( rotates the tetronimo object when the key is pressed. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none )
    # Created ( 22 / 09 / 22 )
    def keyUp(self):
        self.currentTetromino.rotateTetromino()
        self.currentTetromino.translate()
        if self.board.collision(self.currentTetromino.shape) or self.board.collisionLeftRight(
                self.currentTetromino.shape, "both"):
            self.currentTetromino.horizontalFlip()
            self.currentTetromino.transpose()

    # FunName ( Creates Next Tetronimo Function )
    # Desc ( This function generates the next tetronimo object. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none )
    # Created ( 22 / 09 / 22 )
    def generateNext(self):
        self.nextTetromino = Tetromino(self.currentTimeScale, start=self.board.startingCoordinates)

    # FunName ( Force Tetronimo Object To Floor Function )
    # Desc ( This function forces the tetronimo object to the bottom of the playing field. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( True or false depending on collision detection )
    # Created ( 22 / 09 / 22 )
    def keySpace(self):
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

        # FunName ( increases the acceleration )
        # Desc ( This function accelerates the object. )
        # Author ( Jake )
        # Parameters ( none )
        # Return Values ( the toggle indicator )
        # Created ( 22 / 09 / 22 )

    def keyDown(self, sentData):
        if sentData:
            self.currentTimeScale = 0.1
            sentData = False
        else:
            self.currentTimeScale = 1
            sentData = True

        return sentData

    # FunName ( Held Object Function )
    # Desc ( This function holds an object or creates a new object and stores the previous object
    # depending on if it has been used before. It will also check if the object has been switched on that "turn". )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( true or false depending on collision detection )
    # Created ( 22 / 09 / 22 )
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

    # FunName ( Move Down Function )
    # Desc ( This function will move the object down - if that is not possible,
    # it creates a new object and fixes the previous in its place.)
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( Collision True False Data )
    # Created ( 22 / 09 / 22 )
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

    """
    # FunName ( Current Speed Calculator )
    # Desc ( Calculates the rate at which tetronimo objects fall. Is classified as a variable. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( Current Speed )
    # Created ( 22 / 09 / 22 )
    @property
    def currentTimeScale(self):

        return 1;

        if self.clearedCount == 0:
            return 1
        else:
            return 1 + self.clearedCount / 25
    """
