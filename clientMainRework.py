import pygame
import random


class Tetromino:

    # FunName ( Init - Startup Function )
    # Desc ( Sets up the object with required parameters needed by other methods later in the class, "initializes" the code )
    # Author ( Jake )
    # Parameters ( current time value, sets it if not taken as var )
    # Return Values ( none, defining variables not returning them )
    # Created ( 10 / 06 / 22 )
    def __init__(self, curTimeVal=1, start=(0, 0)):

        self.transposedList = []
        self._shapeList = {
            "tBracket": [(-1, 0), (0, 0), (1, 0), (0, 1)],
            "line": [(-1, 0), (0, 0), (1, 0), (2, 0)],
            "square": [(-1, 0), (0, 0), (-1, 1), (0, 1)],
            "lBracketLeft": [(-1, 0), (0, 0), (1, 0), (-1, 1)],
            "lBracketRight": [(-1, 0), (0, 0), (1, 0), (1, 1)],
            "sBracketLeft": [(0, 0), (1, 0), (-1, 1), (0, 1)],
            "sBracketRight": [(-1, 0), (0, 0), (0, 1), (1, 1)]
        }
        self._shape = random.choice(list(self._shapeList.values()))
        self._trueShape = None
        self.xMod = start[0]
        self.yMod = start[1]
        self.translate()
        print(f"Creating tetromino at {self.xMod}/{self.yMod}")
        self.fixedTime = curTimeVal
        self.blockSize = 30, 30

        self.colour = random.choice([
            "assets/tetrisBlockBlue.png",
            "assets/tetrisBlockGreen.png",
            "assets/tetrisBlockYellow.png",
            "assets/tetrisBlockRed.png",
            "assets/tetrisBlockPurple.png"
        ])

    def state(self):
        return {"shape": self._trueShape, "blockSize": self.blockSize, "colour": self.colour}

    # FunName ( Transpose Function )
    # Desc ( transposes an object via swapping x and y position )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none, defining variables not returning them )
    # Created ( 10 / 06 / 22 )
    def transpose(self):

        for x, y in self._shape:
            self.transposedList.append((y, x))
        self._shape = self.transposedList
        self.transposedList = []

    # FunName ( Object Flip Horizontal Var )
    # Desc ( Flips an object via the x-axis - hence horizontal )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none, defining variables not returning them )
    # Created ( 10 / 06 / 22 )
    def horizontalFlip(self):

        for x, y in self._shape:
            self.transposedList.append((-x, y))
        self._shape = self.transposedList
        self.transposedList = []

    # FunName ( rotationOfObject )
    # Desc ( Combines the transpose and flip functions to create a single rotate function. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none, defining variables not returning them )
    # Created ( 10 / 06 / 22 )
    def rotateTetromino(self):

        tempList = []
        for x, y in self._shape:
            self.transposedList.append((y, x))

        for x, y in self.transposedList:
            tempList.append((-x, y))

        self.transposedList = tempList
        self._shape = self.transposedList
        self.transposedList = []

    # FunName ( Move Object Up )
    # Desc ( alters the y modifier for the translation function, allowing the object to move up. This should only be used with CLIPPING ISSUES )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none, defining variables not returning them )
    # Created ( 10 / 06 / 22 )
    def moveUp(self):

        self.yMod -= 1

    # FunName ( Move Object Down )
    # Desc ( alters the y modifier for the translation function, allowing the object to move down. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none, defining variables not returning them )
    # Created ( 10 / 06 / 22 )
    def moveDown(self):

        self.yMod += 1

    # FunName ( Move Object Right )
    # Desc ( alters the x modifier for the translation function, allowing the object to move right. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none, defining variables not returning them )
    # Created ( 10 / 06 / 22 )
    def moveRight(self):

        self.xMod += 1

    # FunName ( Move Object Left )
    # Desc ( alters the x modifier for the translation function, allowing the object to move left. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none, defining variables not returning them )
    # Created ( 10 / 06 / 22 )
    def moveLeft(self):

        self.xMod -= 1

    # FunName ( translate Object Function )
    # Desc ( uses the shape variable and alters it with the modifier data to be represented within pygame. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none, defining variables not returning them )
    # Created ( 10 / 06 / 22 )
    def translate(self):

        self._trueShape = []

        for x, y in self._shape:
            self._trueShape.append((x + self.xMod, y + self.yMod))

    # FunName ( shape function defined as variable )
    # Desc ( Utilises the @property to make this function a variable, is used for the pygameMain file to access _trueShape. It does NOT allow for changes to _trueShape )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( ._trueShape variable as .shape due to @property )
    # Created ( 10 / 06 / 22 )
    @property
    def shape(self):

        return self._trueShape


class Board:

    # FunName ( Init - Startup Function )
    # Desc ( Sets up the object with required parameters needed by other methods later in the class, "initializes" the code )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none, defining variables not returning them )
    # Created ( 10 / 06 / 22 )
    def __init__(self):

        self.startingCoordinates = [6, 3]
        self.boardSize = [10, 20]
        self.fixed = []

    # FunName ( collision function )
    # Desc ( takes an object and checks relative to the board to see if it collides with either the floor or the list of fixed position items. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( True - If collision present )
    # Created ( 10 / 06 / 22 )
    def collision(self, itemObject):

        for x, y in itemObject:

            if y > self.boardSize[1]:
                return True
            else:
                for (xVal, yVal) in self.fixed:
                    if x == xVal and y == yVal:
                        return True

    # FunName ( collision function for sides )
    # Desc ( checks for collision with either the left / right side and/or the fixed position of items. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( True - If collision present )
    # Created ( 10 / 06 / 22 )
    def collisionLeftRight(self, itemObject, direction):

        for x, y in itemObject:

            if x > self.boardSize[0] and direction == "right":
                return True
            elif x < 1 and direction == "left":
                return True
            elif x > self.boardSize[0] and direction == "both" or x < 1 and direction == "both":
                return True
            else:
                for (xVal, yVal) in self.fixed:
                    if x == xVal and y == yVal:
                        return True

    # FunName ( set Completed blocks function )
    # Desc ( takes the object and copies it into the active fixed list to be used for collision. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none, appending data not returning it )
    # Created ( 10 / 06 / 22 )
    def setFixed(self, itemObject):

        for i in itemObject:
            self.fixed.append(i)


class PygameData:
    # FunName ( Init - Startup Function )
    # Desc ( Sets up the object with required parameters needed by other methods later in the class, "initializes" the code )
    # Author ( Jake )
    # Parameters ( logo - this is the name of the logo image for it to find in the directory )
    # Return Values ( none, defining variables not returning them as well as running functions )
    # Created ( 10 / 06 / 22 )
    def __init__(self, logo):

        pygame.init()
        self.totalGameSize = [360, 660]
        self.totalMenuSize = [720, 660]
        self.displayScreen = pygame.display.set_mode(self.totalMenuSize)
        self.clock = pygame.time.Clock()
        self.ico = pygame.image.load(logo)
        pygame.display.set_icon(self.ico)
        pygame.display.set_caption("Tetris")
        pygame.mixer.init()
        self.bgMusic = pygame.mixer.Sound("assets/tetrisMusic.ogg")
        self.volLevel = 0.0
        self.bgMusic.set_volume(self.volLevel)
        self.bgMusic.play(loops=-1)

    # FunName ( draw border object function )
    # Desc ( takes in border image and defines it by the block size, blitting image to the screen. )
    # Author ( Jake )
    # Parameters ( blockSize - this is the pixel size of your blocks.)
    # Return Values ( none, defining variables not returning them )
    # Created ( 10 / 06 / 22 )
    def drawBorder(self, blockSize, borderImage):

        borderBlock = pygame.image.load(borderImage)

        for x in range((self.totalGameSize[0] // blockSize[0])):

            for y in range((self.totalGameSize[1] // blockSize[1])):
                if x == 0 or x == 11 or y == 0 or y == 21:
                    self.displayScreen.blit(borderBlock, ((x * blockSize[0]), (y * blockSize[1])))

    # FunName ( object Draw function )
    # Desc ( takes data to draw an object with size, image and piece data provided.  )
    # Author ( Jake )
    # Parameters ( blockSize - this is the square pixel size, one int val, piece data-this is a list of the x, y coordinates, and the image is what we are blitting to the screen, image, piece data )
    # Return Values ( none, is blitting object to screen instead. )
    # Created ( 10 / 06 / 22 )
    def drawObject(self, blockSize, pieceData, image):

        piece = pygame.image.load(image)
        for (x, y) in pieceData:
            self.displayScreen.blit(piece, ((x * blockSize[0]), (y * blockSize[1])))

    # FunName ( object Draw function )
    # Desc ( takes data to draw an object with size, image and piece data provided. FOR THE MENU - NEXT AND HOLD PIECES ONLY!!!! IMPORTANT )
    # Author ( Jake )
    # Parameters ( blockSize - this is the square pixel size, one int val, piece data-this is a list of the x, y coordinates, and the image is what we are blitting to the screen, image, piece data )
    # Return Values ( none, is blitting object to screen instead. )
    # Created ( 16 / 06 / 22 )
    def drawObjectRight(self, coordinates, blockSize, pieceData, image):

        piece = pygame.image.load(image)
        for (x, y) in pieceData:
            self.displayScreen.blit(piece, ((x * blockSize[0]) + coordinates[0], (y * blockSize[1]) + coordinates[1]))

    # FunName ( menu Right Draw function )
    # Desc ( takes data to draw an object with size, image and piece data provided.  )
    # Author ( Jake )
    # Parameters ( image, piece Data)
    # Return Values ( none, is blitting object to screen instead. )
    # Created ( 16 / 06 / 22 )
    def drawRightMenu(self, pieceData, image):

        piece = pygame.image.load(image)
        self.displayScreen.blit(piece, pieceData)

    # FunName ( text mapping to screen fun )
    # Desc ( takes data to draw text to a given location )
    # Author ( Jake )
    # Parameters ( image, piece Data)
    # Return Values ( none, is blitting object to screen instead. )
    # Created ( 16 / 06 / 22 )
    def blitText(self, coordinates, data, fontData):

        fontR = pygame.font.SysFont(fontData[0], fontData[1])
        textRendered = fontR.render(data, True, (255, 255, 255))
        self.displayScreen.blit(textRendered, coordinates)

    # FunName ( menu Right Draw function )
    # Desc ( changes the volume level  )
    # Author ( Jake )
    # Parameters ( None )
    # Return Values ( none, is adjusting vol )
    # Created ( 16 / 06 / 22 )
    def volDecr(self):
        if self.volLevel > 0.05:
            self.volLevel -= 0.05
        self.bgMusic.set_volume(self.volLevel)

    # FunName ( volume decrease function )
    # Desc ( changes the volume level  )
    # Author ( Jake )
    # Parameters ( None )
    # Return Values ( none, is adjusting vol )
    # Created ( 16 / 06 / 22 )
    def volIncr(self):
        if self.volLevel < 0.95:
            self.volLevel += 0.05
        self.bgMusic.set_volume(self.volLevel)

    # FunName ( update screen function )
    # Desc ( update the screen in pygame and sets framerate. )
    # Author ( Jake )
    # Parameters ( none )
    # Return Values ( none, just running other functions )
    # Created ( 10 / 06 / 22 )
    def refreshScreen(self):

        self.clock.tick(60)
        pygame.display.flip()


if __name__ == "__main__":
    pass
