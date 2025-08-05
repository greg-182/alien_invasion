import pygame

class TextInput:
    """A class to manage text input for player names."""
    
    def __init__(self, ai_game, msg):
        """Initialize text input attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        
        # Set dimensions and properties of the input box
        self.width, self.height = 200, 50
        self.input_box_color = (100, 100, 100)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 28)
        
        # Build the input box rect and position it below the play button
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y = self.screen_rect.center[1] + 70
        
        # Placeholder message
        self.msg = msg
        self.text = ''
        self.active = False
        
        # Prepare the initial message image
        self._prep_placeholder()
        
    def _prep_placeholder(self):
        """Turn the placeholder message into a rendered image."""
        if not self.text and not self.active:
            self.placeholder_image = self.font.render(self.msg, True, 
                self.text_color, self.input_box_color)
            self.placeholder_rect = self.placeholder_image.get_rect()
            self.placeholder_rect.center = self.rect.center
        
    def _prep_text(self):
        """Turn the text into a rendered image."""
        self.text_image = self.font.render(self.text, True, 
            self.text_color, self.input_box_color)
        self.text_rect = self.text_image.get_rect()
        self.text_rect.center = self.rect.center
        
    def handle_event(self, event):
        """Handle keyboard and mouse events for the text input."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state if the user clicks on the input box
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False
        
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                # Return the text when Enter is pressed
                return self.text
            elif event.key == pygame.K_BACKSPACE:
                # Remove the last character when Backspace is pressed
                self.text = self.text[:-1]
            else:
                # Add the character to the text (limit to 15 characters)
                if len(self.text) < 15:
                    self.text += event.unicode
            
            # Re-render the text
            self._prep_text()
        
        return None
        
    def draw(self):
        """Draw the input box and current text."""
        # Draw the input box
        pygame.draw.rect(self.screen, self.input_box_color, self.rect, 0)
        
        # Draw the text or placeholder
        if self.text:
            self._prep_text()
            self.screen.blit(self.text_image, self.text_rect)
        else:
            self._prep_placeholder()
            self.screen.blit(self.placeholder_image, self.placeholder_rect)
