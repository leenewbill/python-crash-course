"""
Module Name: game_stats.py
Description: 
Exports: class GameStats
"""

import json

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False

        # Read the high score from the JSON. 
        #   If the JSON doesn't exist, set high_score to 0.
        try:
            with open(self.settings.high_score_json) as f:
                self.high_score = json.load(f)
        except FileNotFoundError:
            self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0

        self.level = 1
        if self.settings.difficulty == 'medium':
            self.increase_level(3)
        elif self.settings.difficulty == 'hard':
            self.increase_level(7)

    def increase_level(self, num_times=1):
        """
        Increase the game speed and the level a number of times, then update the
            level text.
        """
        for i in range(num_times):
            self.settings.increase_speed()
            self.level += 1
