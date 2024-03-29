class Settings():
    """A class to store all the settings for Alien Invasion."""

    def __init__(self):
        """Initialize games settings."""
        # Screen Settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed_factor = 5

        # Bullet Settings
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

