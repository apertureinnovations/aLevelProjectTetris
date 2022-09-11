import threading
from datetime import datetime
import pygame
import json
from clientMainRework import PygameData
from gameObjects import TGame


def pygameProgram():
    gameParameters = PygameData("assets/tetrisLogo.png")
    lastMoveDown = 0
    running = True
    gameObject = TGame()
    blockSize = json.loads(gameObject.currentTetrominoState())
    while running:

        gameParameters.displayScreen.fill((0, 0, 0))

        gameParameters.drawBorder(blockSize["blockSize"], "assets/tetrisBlock.png")

        gameParameters.drawRightMenu((360, 0), "assets/menuRight.png")

        nextState = json.loads(gameObject.currentNextState())

        gameParameters.drawObjectRight((440, 450),
                                       blockSize["blockSize"],
                                       nextState["shape"],
                                       nextState["colour"])

        if gameObject.held:

            holdState = json.loads(gameObject.currentHoldState())
            gameParameters.drawObjectRight((560, 240),
                                           blockSize["blockSize"],
                                           holdState["shape"],
                                           holdState["colour"])

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
        currentSpeed = json.loads(gameObject.grabTime())
        if (datetime.timestamp(datetime.now()) - lastMoveDown) > currentSpeed:
            lastMoveDown = datetime.timestamp(datetime.now())

            running = gameObject.moveAutomatic()

        gameObject.currentTetromino.translate()

        scoreData = json.loads(gameObject.getScores())

        gameParameters.blitText((380, 580), str(scoreData["clearCount"]), ["arial", 40])
        gameParameters.blitText((450, 580), ("Lines Cleared: " + str(scoreData["currentScore"])), ["arial", 40])

        tetraState = json.loads(gameObject.currentTetrominoState())

        gameState = json.loads(gameObject.currentBoardState())

        gameParameters.drawObject(blockSize["blockSize"],
                                  tetraState["shape"],
                                  tetraState["colour"])

        gameParameters.drawObject(blockSize["blockSize"], gameState["boardFixed"],
                                  "assets/tetrisBlockComplete.png")

        gameParameters.refreshScreen()
        # print(f"Looped, running is now {running}")

    pygame.quit()


def MainProgram():
    threading.Thread(target=pygameProgram, args=()).start()

    pass


MainProgram()
