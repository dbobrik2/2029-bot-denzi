from game_state import GameState

class GameManager ():
    """
        Responsible for handling game state, process and players
    """
    def __init__(self, game_title, game_version):
        """Show game intro to the user"""
        self.game_title = "2029р."
        self.game_version = 1.0

    def start(self):
        """Starts game. Shows game info to the user"""
        print(f"{self.game_title} v{self.game_version}")
        print("Game started.")
        self.game_state = GameState.START