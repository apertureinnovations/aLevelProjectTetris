from clientMainRework import Board, Tetromino
class TGame(object):
    def __init__(self):
        """ Initialise all game data """
        self.board=Board()
        self.score=0
        self.held=None
        self.heldFresh=True
        self.clearedCount=0
        self.currentTetromino=Tetromino(self.currentTimeScale)
        self.scoreList = [0, 100, 300, 500, 800]
        self.nextTetromino=Tetromino(self.currentTimeScale)
        #score
        #board
        #held
        #etc
        pass


    def key_right(self):
        self.currentTetromino.moveRight()
        self.currentTetromino.translate()
        if self.board.collisionLeftRight(self.currentTetromino.shape, "right"):
                        self.currentTetromino.moveLeft()
                        self.currentTetromino.translate()

    
    @property
    def currentTimeScale(self):
        if self.clearedCount==0:
            return 1
        else:
            return 1+self.clearedCount/25
    
    def left(self):
        pass
    def right(self):
        pass
    def hold(self):
