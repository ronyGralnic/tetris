# gamewindow.py
import pygame
from playarea import PlayArea

class GameWindow:
    def __init__(self):
        self.screenWidth = 800
        self.screenHeight = 700
        self.gameArea = PlayArea()
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        pygame.display.set_caption("Tetris")
        pygame.font.init()
        self.font = pygame.font.SysFont("comicsans", 60)
        self.topLeftX = 50
        self.topLeftY = 50

    def drawWindow(self, score=0, lastScore=0, currPiece=None):
        self.screen.fill((0, 0, 0))
        # ... draw title, score, etc.

        # Draw the locked grid
        for i in range(len(self.gameArea.grid)):
            for j in range(len(self.gameArea.grid[i])):
                pygame.draw.rect(self.screen, self.gameArea.grid[i][j],
                                 (self.topLeftX + j * self.gameArea.gameAreaBlockSize,
                                  self.topLeftY + i * self.gameArea.gameAreaBlockSize,
                                  self.gameArea.gameAreaBlockSize,
                                  self.gameArea.gameAreaBlockSize), 0)

        # Draw the currently moving piece separately
        if currPiece is not None:
            for pos in currPiece.positions:
                x, y = pos
                if y > -1:
                    pygame.draw.rect(self.screen, currPiece.color,
                                     (self.topLeftX + x * self.gameArea.gameAreaBlockSize,
                                      self.topLeftY + y * self.gameArea.gameAreaBlockSize,
                                      self.gameArea.gameAreaBlockSize,
                                      self.gameArea.gameAreaBlockSize), 0)

        # Draw border
        pygame.draw.rect(self.screen, (255, 0, 0),
                         (self.topLeftX, self.topLeftY, self.gameArea.gameAreaWidth, self.gameArea.gameAreaHeight), 4)

        self.gameArea.drawGrid(self.screen, self.topLeftX, self.topLeftY)

    def drawNextShape(self, currPiece):
        font = pygame.font.SysFont("comicsans", 30)
        label = font.render('Next Shape', 1, (255,255,255))
        startX = self.topLeftX + self.gameArea.gameAreaWidth + 50
        startY = self.topLeftY + 100

        format = currPiece.shape[currPiece.rotation % len(currPiece.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    pygame.draw.rect(self.screen, currPiece.color,
                                     (startX + j * self.gameArea.gameAreaBlockSize,
                                      startY + i * self.gameArea.gameAreaBlockSize,
                                      self.gameArea.gameAreaBlockSize,
                                      self.gameArea.gameAreaBlockSize), 0)

        self.screen.blit(label, (startX+10, startY-30))

    def drawTextMiddle(self, text, size, color):
        font = pygame.font.SysFont("comicsans", size, bold=True)
        label = font.render(text, 1, color)
        self.screen.blit(label, (self.topLeftX + self.gameArea.gameAreaWidth/2 - label.get_width()/2,
                                 self.topLeftY + self.gameArea.gameAreaHeight/2 - label.get_height()/2))
