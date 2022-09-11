import threading
from datetime import datetime
import pygame
from clientMainRework import Tetromino, Board, PygameData
from gameObjects import TGame


def scoreSys(boardParameters, curScore=0):
    for y in range(boardParameters.boardSize[1]):
        y += 1
        for x in range(boardParameters.boardSize[0]):
            x += 1
            if not (x, y) in boardParameters.fixed:
                break
        else:
            tempList = []
            for xVal, yVal in boardParameters.fixed:
                if yVal < y:
                    tempList.append((xVal, yVal + 1))
                elif yVal > y:
                    tempList.append((xVal, yVal))
            boardParameters.fixed = tempList
            curScore += 1

            curScore = scoreSys(boardParameters, curScore)

    return curScore


def nextPiece(currentMultiplierTimeValue):
    nextPieceObject = Tetromino(currentMultiplierTimeValue)
    return nextPieceObject


def pygameProgram():
    currentScore = 0
    scoreList = [0, 100, 300, 500, 800]
    boardParameters, gameParameters = Board(), PygameData("assets/tetrisLogo.png")
    holdingPieceData = None
    holdCounter = 0
    currentLinesCleared = 0
    currentMultiplierTimeValue = 1
    tetrominoObject = Tetromino(currentMultiplierTimeValue, boardParameters.startingCoordinates)
    #tetrominoObject.xMod += (boardParameters.startingCoordinates[0])
    #tetrominoObject.yMod += (boardParameters.startingCoordinates[1])
    nextPieceObject = 0
    lastMoveDown = 0
    running = True
    target = 0


    gameObject=TGame()

    
    while running:

        gameParameters.displayScreen.fill((0, 0, 0))
        gameParameters.drawBorder(tetrominoObject.blockSize, "assets/tetrisBlock.png")

        gameParameters.drawRightMenu((360, 0), "assets/menuRight.png")

        # if nextPieceObject == tetrominoObject or nextPieceObject == 0:
        #     nextPieceObject = nextPiece(currentMultiplierTimeValue)

        #nextPieceObject.translate()
        gameParameters.drawObjectRight((440, 450),
                                       gameObject.nextTetromino.blockSize,
                                       gameObject.nextTetromino.shape,
                                       gameObject.nextTetromino.colour)

        if gameObject.held:
            #holdingPieceData.translate()
            gameParameters.drawObjectRight((560, 240),
                                           gameObject.held.blockSize,
                                           gameObject.held.shape,
                                           gameObject.held.colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    gameObject.key_right()

                if event.key == pygame.K_LEFT:
                    tetrominoObject.moveLeft()
                    tetrominoObject.translate()
                    if boardParameters.collisionLeftRight(tetrominoObject.shape, "left"):
                        tetrominoObject.moveRight()
                        tetrominoObject.translate()

                if event.key == pygame.K_UP:
                    tetrominoObject.rotateTetromino()
                    tetrominoObject.translate()
                    if boardParameters.collision(tetrominoObject.shape) or boardParameters.collisionLeftRight(
                            tetrominoObject.shape, "both"):
                        tetrominoObject.horizontalFlip()
                        tetrominoObject.transpose()

                if event.key == pygame.K_DOWN:
                    while not boardParameters.collision(tetrominoObject.shape):
                        tetrominoObject.moveDown()
                        tetrominoObject.translate()

                    tetrominoObject.moveUp()
                    tetrominoObject.translate()
                    boardParameters.setFixed(tetrominoObject.shape)

                    nextPieceObject.xMod += (boardParameters.startingCoordinates[0])
                    nextPieceObject.yMod += (boardParameters.startingCoordinates[1])
                    tetrominoObject = nextPieceObject
                    tetrominoObject.translate()

                    if boardParameters.collision(tetrominoObject.shape):
                        running = False
                    holdCounter = 0

                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_h:
                    if holdCounter < 1:
                        if holdingPieceData is None:
                            holdingPieceData = tetrominoObject
                            holdingPieceData.xMod, holdingPieceData.yMod = 0, 0
                            nextPieceObject.xMod += (boardParameters.startingCoordinates[0])
                            nextPieceObject.yMod += (boardParameters.startingCoordinates[1])
                            tetrominoObject = nextPieceObject

                            if boardParameters.collision(tetrominoObject.shape):
                                running = False
                            holdCounter += 1

                        else:
                            tempVal = tetrominoObject
                            tetrominoObject = holdingPieceData
                            holdingPieceData = tempVal
                            holdingPieceData.xMod, holdingPieceData.yMod = 0, 0
                            tetrominoObject.xMod += (boardParameters.startingCoordinates[0])
                            tetrominoObject.yMod += (boardParameters.startingCoordinates[1])
                            tetrominoObject.translate()
                            if boardParameters.collision(tetrominoObject.shape):
                                running = False
                            holdCounter += 1

                if event.key == pygame.K_z:
                    gameParameters.volDecr()

                if event.key == pygame.K_x:
                    gameParameters.volIncr()

        if (datetime.timestamp(datetime.now()) - lastMoveDown) > tetrominoObject.fixedTime:
            lastMoveDown = datetime.timestamp(datetime.now())

            tetrominoObject.moveDown()
            tetrominoObject.translate()
            if boardParameters.collision(tetrominoObject.shape):
                tetrominoObject.moveUp()
                tetrominoObject.translate()
                boardParameters.setFixed(tetrominoObject.shape)

                nextPieceObject.xMod += (boardParameters.startingCoordinates[0])
                nextPieceObject.yMod += (boardParameters.startingCoordinates[1])
                tetrominoObject = nextPieceObject
                tetrominoObject.translate()
                if boardParameters.collision(tetrominoObject.shape):
                    running = False
                holdCounter = 0

        tetrominoObject.translate()

        scoreMultiplier = scoreSys(boardParameters)

        currentLinesCleared += scoreMultiplier
        currentScore += scoreList[scoreMultiplier]

        for i in range(scoreMultiplier):
            if currentMultiplierTimeValue > 0.5:
                currentMultiplierTimeValue -= 0.075
            elif currentMultiplierTimeValue > 0.25:
                currentMultiplierTimeValue -= 0.025
            elif currentMultiplierTimeValue > 0.1:
                currentMultiplierTimeValue -= 0.01

        gameParameters.blitText((380, 580), str(currentScore), ["arial", 40])
        gameParameters.blitText((450, 580), ("Lines Cleared: " + str(currentLinesCleared)), ["arial", 40])

        gameParameters.drawObject(tetrominoObject.blockSize, tetrominoObject.shape, tetrominoObject.colour)

        gameParameters.drawObject(tetrominoObject.blockSize, boardParameters.fixed, "assets/tetrisBlockComplete.png")

        gameParameters.refreshScreen()

        gamePackageData = [boardParameters, tetrominoObject, scoreMultiplier, target]

    pygame.quit()


def MainProgram():
    threading.Thread(target=pygameProgram, args=()).start()

    pass


MainProgram()
