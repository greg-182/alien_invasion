import json


class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Save high score to a file."""
        filename = 'high_score.json'
        with open(filename, 'w') as f:
            json.dump(self.high_score, f)

    def load_high_score(self):
        """Load the high score from file."""
        filename = 'high_score.json'
        try:
            with open(filename) as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return 0
        except FileNotFoundError:
            return 0
