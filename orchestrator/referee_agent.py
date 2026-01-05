from services.validation_service.validate_move import validate_move
from services.game_logic_service.resolve_round import resolve_round
from services.bot_service.bot_strategy import choose_bot_move
from services.state_service.game_state import GameState


class RefereeAgent:
    def __init__(self, state: GameState):
        self.state = state

    def explain_rules(self):
        print(
            "Rules: Best of 3 rounds. Moves: rock, paper, scissors.\n"
            "Each player may use 'bomb' once per game.\n"
            "Bomb beats everything. Bomb vs bomb is a draw.\n"
            "Invalid input wastes the round.\n"
        )

    def play_round(self, user_input: str):
        validation = validate_move(user_input, self.state.user_bomb_used)

        print(f"\nRound {self.state.round_number}/3")

        if not validation["valid"]:
            print(f"Invalid input: {validation['reason']}")
            print("Round wasted.")
            self.state.advance_round()
            return

        user_move = validation["move"]
        bot_move = choose_bot_move(self.state.bot_bomb_used)

        result = resolve_round(user_move, bot_move)

        if user_move == "bomb":
            self.state.user_bomb_used = True
        if bot_move == "bomb":
            self.state.bot_bomb_used = True

        if result == "user":
            self.state.user_score += 1
            outcome = "You win this round"
        elif result == "bot":
            self.state.bot_score += 1
            outcome = "Bot wins this round"
        else:
            outcome = "This round is a draw"

        print(f"You played: {user_move}")
        print(f"Bot played: {bot_move}")
        print(f"Result: {outcome}")
        print(f"Score → You: {self.state.user_score} | Bot: {self.state.bot_score}")

        self.state.advance_round()

    def conclude_game(self):
        print("\nGame Over")
        if self.state.user_score > self.state.bot_score:
            print("Final Result: User wins")
        elif self.state.bot_score > self.state.user_score:
            print("Final Result: Bot wins")
        else:
            print("Final Result: Draw")
