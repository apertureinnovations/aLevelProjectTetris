import threading
from datetime import datetime
import pygame
from clientMainRework import PygameData
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


def pygameProgram():
    scoreList = [0, 100, 300, 500, 800]
    gameParameters = PygameData("assets/tetrisLogo.png")
    # holdingPieceData = None
    # holdCounter = 0
    # currentLinesCleared = 0
    # currentMultiplierTimeValue = 1
    # tetrominoObject = Tetromino(currentMultiplierTimeValue, boardParameters.startingCoordinates)
    # tetrominoObject.xMod += (boardParameters.startingCoordinates[0])
    # tetrominoObject.yMod += (boardParameters.startingCoordinates[1])
    # nextPieceObject = 0
    lastMoveDown = 0
    running = True

    gameObject = TGame()

    while running:

        gameParameters.displayScreen.fill((0, 0, 0))
        gameParameters.drawBorder(gameObject.currentTetromino.blockSize, "assets/tetrisBlock.png")

        gameParameters.drawRightMenu((360, 0), "assets/menuRight.png")

        # if nextPieceObject == tetrominoObject or nextPieceObject == 0:
        #     nextPieceObject = nextPiece(currentMultiplierTimeValue)

        # nextPieceObject.translate()
        gameParameters.drawObjectRight((440, 450),
                                       gameObject.nextTetromino.blockSize,
                                       gameObject.nextTetromino.shape,
                                       gameObject.nextTetromino.colour)

        if gameObject.held:
            # holdingPieceData.translate()
            gameParameters.drawObjectRight((560, 240),
                                           gameObject.held.blockSize,
                                           gameObject.held.shape,
                                           gameObject.held.colour)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    gameObject.keyRight()

                if event.key == pygame.K_LEFT:
                    gameObject.keyLeft()

                if event.key == pygame.K_UP:
                    gameObject.keyUp()

                if event.key == pygame.K_DOWN:
                    running = gameObject.keyDown()

                if event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_h:
                    running = gameObject.keyHold()

                if event.key == pygame.K_z:
                    gameParameters.volDecr()

                if event.key == pygame.K_x:
                    gameParameters.volIncr()

        if (datetime.timestamp(datetime.now()) - lastMoveDown) > gameObject.currentTetromino.fixedTime:
            lastMoveDown = datetime.timestamp(datetime.now())

            running = gameObject.moveAutomatic()

        gameObject.currentTetromino.translate()

        scoreMultiplier = scoreSys(gameObject.board)

        gameObject.clearedCount += scoreMultiplier
        gameObject.currentScore += scoreList[scoreMultiplier]

        """
        for i in range(scoreMultiplier):
            if currentMultiplierTimeValue > 0.5:
                currentMultiplierTimeValue -= 0.075
            elif currentMultiplierTimeValue > 0.25:
                currentMultiplierTimeValue -= 0.025
            elif currentMultiplierTimeValue > 0.1:
                currentMultiplierTimeValue -= 0.01
        """

        gameParameters.blitText((380, 580), str(gameObject.currentScore), ["arial", 40])
        gameParameters.blitText((450, 580), ("Lines Cleared: " + str(gameObject.clearedCount)), ["arial", 40])

        gameParameters.drawObject(gameObject.currentTetromino.blockSize, gameObject.currentTetromino.shape,
                                  gameObject.currentTetromino.colour)

        gameParameters.drawObject(gameObject.currentTetromino.blockSize, gameObject.board.fixed,
                                  "assets/tetrisBlockComplete.png")

        gameParameters.refreshScreen()
        #print(f"Looped, running is now {running}")

    pygame.quit()


def MainProgram():
    threading.Thread(target=pygameProgram, args=()).start()

    pass


MainProgram()
