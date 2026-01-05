VALID_MOVES = {"rock", "paper", "scissors", "bomb"}


def validate_move(move: str, bomb_used: bool) -> dict:
    move = move.lower().strip()

    if move not in VALID_MOVES:
        return {"valid": False, "reason": "Invalid move"}

    if move == "bomb" and bomb_used:
        return {"valid": False, "reason": "Bomb already used"}

    return {"valid": True, "move": move}

