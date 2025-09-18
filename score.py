# score.py
import os

class Score:
    """
    Handles current score and high score tracking in a file.
    """
    def __init__(self):
        self.score = 0
        self.file = "scores.txt"
        # Ensure the score file exists
        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                f.write("0")

    def updateScore(self):
        """
        Update the saved high score if current score is higher.
        """
        max_score = int(self.maxScore())
        if self.score > max_score:
            with open(self.file, 'w') as f:
                f.write(str(self.score))

    def maxScore(self):
        """
        Retrieve the current high score from the file.
        """
        with open(self.file, 'r') as f:
            lines = f.readlines()
            return lines[0].strip() if lines else "0"
