import random

MOVES = ["rock", "paper", "scissors", "bomb"]


def choose_bot_move(bomb_used: bool) -> str:
    if bomb_used:
        return random.choice(["rock", "paper", "scissors"])
    return random.choice(MOVES)

