# shapes.py
import random

SHAPES = [
    [[".....",
      ".....",
      "..00.",
      ".00..",
      "....."],
     [".....",
      "..0..",
      "..00.",
      "...0.",
      "....."]],
    [[".....",
      ".....",
      ".00..",
      "..00.",
      "....."],
     [".....",
      "..0..",
      ".00..",
      ".0...",
      "....."]],
    [[".....",
      ".....",
      ".00..",
      ".00..",
      "....."]],
    [[".....",
      "...0.",
      ".000.",
      ".....",
      "....."],
     [".....",
      "..0..",
      "..0..",
      "..00.",
      "....."]],
    [[".....",
      ".0...",
      ".000.",
      ".....",
      "....."],
     [".....",
      "..00.",
      "..0..",
      "..0..",
      "....."]],
]

COLORS = [(0,255,0),(255,0,0),(0,0,255),(255,255,0),(255,165,0)]

class Piece:
    def __init__(self, x, y, shape):
        self.xCor = x
        self.yCor = y
        self.shape = shape
        self.color = COLORS[SHAPES.index(shape)]
        self.rotation = 0
        self.positions = []

    def convertShapeFormat(self):
        self.positions = []
        format = self.shape[self.rotation % len(self.shape)]
        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == "0":
                    self.positions.append((self.xCor + j, self.yCor + i))
        return self.positions

class Shapes:
    def __init__(self):
        self.shapes = SHAPES

    def getShape(self):
        shape = random.choice(self.shapes)
        return Piece(3, -3, shape)
