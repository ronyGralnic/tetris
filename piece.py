from shapes import  Shapes
class Piece:

    def __init__(self, x, y, shape):


        self.xCor = x

        self.yCor = y
        self.shape = shape


        self.color = shape.shapesColorsLobby[shape]

        #for each up arrow ey press, 1 will be added
        self.rotation = 0

        self.positions = []


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
            
