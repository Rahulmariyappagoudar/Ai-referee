from dataclasses import dataclass
from typing import Dict


@dataclass
class GameState:
    round_number: int = 1
    max_rounds: int = 3

    user_score: int = 0
    bot_score: int = 0

    user_bomb_used: bool = False
    bot_bomb_used: bool = False

    game_over: bool = False

    def advance_round(self):
        self.round_number += 1
        if self.round_number > self.max_rounds:
            self.game_over = True

    def to_dict(self) -> Dict:
        return {
            "round_number": self.round_number,
            "user_score": self.user_score,
            "bot_score": self.bot_score,
            "user_bomb_used": self.user_bomb_used,
            "bot_bomb_used": self.bot_bomb_used,
            "game_over": self.game_over,
        }

