"""
The main function is defined here.
Creates instance of tools.Control(do not change).
adds all game states to state_machine dictionary.
"""

from . import prepare, tools
from .states import splash, game, title

def main():
    """Add states to control here."""
    app = tools.Control(prepare.ORIGINAL_CAPTION)
    state_dict = {"SPLASH"  : splash.Splash(),
                  "TITLE"   : title.Title()
                 }
    app.state_machine.setup_states(state_dict, "SPLASH")
    app.main()