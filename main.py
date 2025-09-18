# main.py
import pygame
from gamewindow import GameWindow
from shapes import Shapes
from score import Score

pygame.init()

def main():
    currGameWindow = GameWindow()
    currShapes = Shapes()
    score = Score()
    lastScore = int(score.maxScore())

    changePiece = False
    run = True
    currPiece = currShapes.getShape()
    nextPiece = currShapes.getShape()

    clock = pygame.time.Clock()

    while run:
        currGameWindow.gameArea.grid = currGameWindow.gameArea.createGrid()
        currGameWindow.gameArea.settings.fallTime += clock.get_time()
        currGameWindow.gameArea.settings.levelTime += clock.get_time()

        clock.tick()
        # Move piece down
        if currGameWindow.gameArea.settings.fallTime/1000 > currGameWindow.gameArea.settings.fallSpeed:
            currGameWindow.gameArea.settings.fallTime = 0
            currPiece.yCor += 1
            currPiece.convertShapeFormat()
            if not currGameWindow.gameArea.validSpace(currPiece):
                currPiece.yCor -= 1
                changePiece = True

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    currPiece.xCor -= 1
                    if not currGameWindow.gameArea.validSpace(currPiece):
                        currPiece.xCor += 1
                if event.key == pygame.K_RIGHT:
                    currPiece.xCor += 1
                    if not currGameWindow.gameArea.validSpace(currPiece):
                        currPiece.xCor -= 1
                if event.key == pygame.K_DOWN:
                    currPiece.yCor += 1
                    if not currGameWindow.gameArea.validSpace(currPiece):
                        currPiece.yCor -= 1
                if event.key == pygame.K_UP:
                    currPiece.rotation += 1
                    if not currGameWindow.gameArea.validSpace(currPiece):
                        currPiece.rotation -= 1

        # Draw piece in grid
        currPiece.convertShapeFormat()
        for pos in currPiece.positions:
            x, y = pos
            if y > -1:
                currGameWindow.gameArea.grid[y][x] = currPiece.color

        if changePiece:
            for pos in currPiece.positions:
                currGameWindow.gameArea.lockedPosition[pos] = currPiece.color
            currPiece = nextPiece
            nextPiece = currShapes.getShape()
            changePiece = False
            score.score += currGameWindow.gameArea.clearRows() * 10
        currGameWindow.drawWindow(score.score, lastScore, currPiece)
        currGameWindow.drawNextShape(nextPiece)

        pygame.display.update()

        if currGameWindow.gameArea.checkLost():
            currGameWindow.drawTextMiddle("You Lost!", 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(2000)
            run = False
            score.updateScore()

    pygame.quit()

if __name__ == "__main__":
    main()
