from shapes import  Shapes
import random

colors = [
    (0, 255, 0),     # green
    (255, 0, 0),     # red
    (0, 0, 255),     # blue
    (255, 255, 0),   # yellow
    (255, 165, 0),   # orange
    (128, 0, 128),   # purple
    (0, 255, 255)    # cyan
]

class Piece:
    def __init__(self, x, y, shape):
        self.xCor = x
        self.yCor = y
        self.shape = shape
        self.color = random.choice(colors)  # <-- random each time
        self.rotation = 0



    def convertShapeFormat(self):

        self.positions = []

        format = self.shape.shapesLobby[self.rotation % len(self.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    self.positions.append((self.xCor + j, self.yCor  + i))

        for i,pos in enumerate(self.positions):
            self.positions[i] = (pos[0]-2, pos[1]-4)

