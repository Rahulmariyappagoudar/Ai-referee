def resolve_round(user_move: str, bot_move: str) -> str:
    if user_move == bot_move:
        return "draw"

    if user_move == "bomb":
        return "user"
    if bot_move == "bomb":
        return "bot"

    wins_against = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }

    return "user" if wins_against[user_move] == bot_move else "bot"

