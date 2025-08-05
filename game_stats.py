import json


class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset.
        self.high_scores = self.load_high_scores()
        self.high_score = self._get_highest_score()
        
        # Player name
        self.player_name = "Player"

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """Save high score to a file."""
        # Only save if player has a score
        if self.score > 0:
            # Check if this player already has a score
            player_found = False
            for i, entry in enumerate(self.high_scores):
                if entry['name'] == self.player_name:
                    # Update if new score is higher
                    if self.score > entry['score']:
                        self.high_scores[i]['score'] = self.score
                    player_found = True
                    break
            
            # Add new player if not found
            if not player_found:
                self.high_scores.append({'name': self.player_name, 'score': self.score})
            
            # Sort high scores by score (highest first)
            self.high_scores.sort(key=lambda x: x['score'], reverse=True)
            
            # Keep only top 10 scores
            if len(self.high_scores) > 10:
                self.high_scores = self.high_scores[:10]
            
            # Save to file
            filename = 'high_scores.json'
            with open(filename, 'w') as f:
                json.dump(self.high_scores, f)

    def load_high_scores(self):
        """Load the high scores from file."""
        filename = 'high_scores.json'
        try:
            with open(filename) as f:
                content = f.read()
                if content:
                    try:
                        return json.loads(content)
                    except json.JSONDecodeError:
                        return []
                else:
                    return []
        except FileNotFoundError:
            return []
            
    def _get_highest_score(self):
        """Get the highest score from the high scores list."""
        if self.high_scores:
            return max(entry['score'] for entry in self.high_scores)
        return 0
