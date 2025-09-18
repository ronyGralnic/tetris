# settings.py

class Settings:
    """
    Stores Tetris game settings such as fall time, fall speed, and level timer.
    """
    def __init__(self):
        self.fallTime = 0       # Time since last block movement
        self.fallSpeed = 0.27   # Seconds per block fall
        self.levelTime = 0      # Timer for increasing difficulty
