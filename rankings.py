import pygame

class Rankings:
    """A class to display player rankings."""
    
    def __init__(self, ai_game):
        """Initialize rankings attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Font settings for rankings
        self.text_color = (30, 30, 30)
        self.title_font = pygame.font.SysFont(None, 48)
        self.entry_font = pygame.font.SysFont(None, 36)
        
        # Position for rankings
        self.rankings_rect = pygame.Rect(0, 0, 300, 400)
        self.rankings_rect.right = self.screen_rect.right - 20
        self.rankings_rect.top = 100
        
        # Background color
        self.bg_color = (180, 180, 180)
        
        # Prepare the rankings
        self.prep_rankings()
        
    def prep_rankings(self):
        """Prepare the rankings display."""
        # Create title
        self.title_image = self.title_font.render("High Scores", True, 
            self.text_color, self.bg_color)
        self.title_rect = self.title_image.get_rect()
        self.title_rect.centerx = self.rankings_rect.centerx
        self.title_rect.top = self.rankings_rect.top + 10
        
        # Create entry images
        self.entry_images = []
        self.entry_rects = []
        
        for i, entry in enumerate(self.stats.high_scores[:10]):
            # Format: "1. PlayerName: 1200"
            rank = i + 1
            name = entry['name']
            score = entry['score']
            text = f"{rank}. {name}: {score}"
            
            entry_image = self.entry_font.render(text, True, 
                self.text_color, self.bg_color)
            entry_rect = entry_image.get_rect()
            entry_rect.centerx = self.rankings_rect.centerx
            entry_rect.top = self.title_rect.bottom + 10 + (i * 35)
            
            self.entry_images.append(entry_image)
            self.entry_rects.append(entry_rect)
    
    def draw(self):
        """Draw the rankings to the screen."""
        # Draw background rectangle
        pygame.draw.rect(self.screen, self.bg_color, self.rankings_rect)
        
        # Draw title
        self.screen.blit(self.title_image, self.title_rect)
        
        # Draw entries
        for i in range(len(self.entry_images)):
            self.screen.blit(self.entry_images[i], self.entry_rects[i])
