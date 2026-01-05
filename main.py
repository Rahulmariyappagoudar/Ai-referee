from orchestrator.referee_agent import RefereeAgent
from services.state_service.game_state import GameState


def main():
    state = GameState()
    agent = RefereeAgent(state)

    agent.explain_rules()

    while not state.game_over:
        user_input = input("Enter your move: ")
        agent.play_round(user_input)

    agent.conclude_game()


if __name__ == "__main__":
    main()
