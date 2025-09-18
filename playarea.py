# playarea.py
import pygame
from settings import Settings

class PlayArea:
    def __init__(self):
        self.gameAreaHeight = 600
        self.gameAreaWidth = int(0.5 * self.gameAreaHeight)  # 300
        self.gameAreaBlockSize = 30
        self.lockedPosition = {}
        self.grid = self.createGrid()
        self.settings = Settings()

    def createGrid(self):
        grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]
        for (x, y), color in self.lockedPosition.items():
            if y >= 0:
                grid[y][x] = color
        return grid

    def drawGrid(self, screen, topLeftX, topLeftY):
        for i in range(len(self.grid)):
            pygame.draw.line(screen, (128,128,128),
                             (topLeftX, topLeftY + i*self.gameAreaBlockSize),
                             (topLeftX + self.gameAreaWidth, topLeftY + i*self.gameAreaBlockSize))
            for j in range(len(self.grid[i])):
                pygame.draw.line(screen, (128,128,128),
                                 (topLeftX + j*self.gameAreaBlockSize, topLeftY),
                                 (topLeftX + j*self.gameAreaBlockSize, topLeftY + self.gameAreaHeight))

    def validSpace(self, currPiece):
        """
        Check if the piece is in a valid position (no collisions with locked positions or boundaries).
        """
        acceptedPos = [(j, i) for i in range(20) for j in range(10) if (i, j) not in self.lockedPosition]

        for pos in currPiece.convertShapeFormat():
            x, y = pos
            if x < 0 or x >= 10 or y >= 20:
                return False
            if (x, y) in self.lockedPosition:
                return False
        return True

    def checkLost(self):
        for pos in self.lockedPosition:
            x, y = pos
            if y < 1:
                return True
        return False

    def clearRows(self):
        """
        Clears completed rows, shifts all above rows down,
        and returns number of rows cleared.
        """
        rowsToClear = []
        for i in range(len(self.grid) - 1, -1, -1):
            if (0, 0, 0) not in self.grid[i]:
                rowsToClear.append(i)

        if not rowsToClear:
            return 0

        # Remove the locked positions in cleared rows
        for row in rowsToClear:
            for j in range(10):
                if (j, row) in self.lockedPosition:
                    del self.lockedPosition[(j, row)]

        # Shift everything above cleared rows down
        rowsToClear.sort()  # ascending
        for row in rowsToClear:
            for key in sorted(list(self.lockedPosition), key=lambda x: x[1]):
                x, y = key
                if y < row:
                    # Move block down by 1 for each cleared row below it
                    newKey = (x, y + 1)
                    self.lockedPosition[newKey] = self.lockedPosition.pop(key)

        return len(rowsToClear)
