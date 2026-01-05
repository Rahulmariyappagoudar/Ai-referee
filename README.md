# AI Game Referee 🎮

An intelligent game referee system that orchestrates and manages game logic, player moves, and bot strategies. This project implements a modular architecture with service-based design patterns for scalable game management.

## Features

- 🤖 **Intelligent Bot Strategy** - AI opponent with configurable difficulty levels
- ✅ **Move Validation** - Real-time validation of player moves
- 📊 **Game State Management** - Central state management for consistency
- 🎯 **Round Resolution** - Automatic game logic resolution
- 🏆 **Score Tracking** - Track player and bot scores with bomb mechanics

## Project Structure

```
ai_game_referee/
├── main.py                          # Entry point and game loop
├── orchestrator/
│   ├── __init__.py
│   └── referee_agent.py            # Central game coordinator
├── services/
│   ├── state_service/
│   │   ├── __init__.py
│   │   └── game_state.py           # Game state management
│   ├── validation_service/
│   │   ├── __init__.py
│   │   └── validate_move.py        # Move validation logic
│   ├── game_logic_service/
│   │   ├── __init__.py
│   │   └── resolve_round.py        # Round resolution logic
│   └── bot_service/
│       ├── __init__.py
│       └── bot_strategy.py         # Bot AI strategy
└── README.md
```

## Architecture

### Core Components

1. **GameState** - Central state container
   - Track round number and max rounds
   - Manage player and bot scores
   - Track bomb usage
   - Flag game over status

2. **RefereeAgent** - Orchestrator
   - Coordinates all services
   - Manages game flow
   - Handles player communication

3. **Services**
   - **State Service**: Centralized game state
   - **Validation Service**: Validates player moves
   - **Game Logic Service**: Executes game rules
   - **Bot Service**: Generates AI moves

## Game Flow

```
1. Initialize GameState and RefereeAgent
2. Explain rules to player
3. Loop until game_over:
   - Get player input
   - Validate move
   - Get bot strategy/move
   - Resolve round (apply game logic)
   - Update scores
   - Display results
   - Advance round
4. Conclude game and announce winner
```

## Usage

### Run the Game

```bash
python main.py
```

### Configuration

Customize game settings in `game_state.py`:

```python
@dataclass
class GameState:
    round_number: int = 1
    max_rounds: int = 3          # Change number of rounds
    user_bomb_used: bool = False
    bot_bomb_used: bool = False
```

## Game Mechanics

- **Rounds**: Configurable number of rounds (default: 3)
- **Scoring**: Points awarded based on round winner
- **Bomb**: Special power-up that can be used once per player
- **Win Condition**: Most points after all rounds

## Technologies

- Python 3.8+
- Dataclasses for state management
- Type hints for code clarity

## Development

### Add New Features

1. Create service in appropriate `services/` subdirectory
2. Implement logic in service module
3. Call service from `referee_agent.py`
4. Update `GameState` if needed

### Modify Game Rules

Edit `services/game_logic_service/resolve_round.py` to implement custom rules.

## Future Enhancements

- [ ] Multiple game modes
- [ ] Difficulty levels for bot
- [ ] Player statistics tracking
- [ ] Network multiplayer support
- [ ] Web UI interface
- [ ] Database integration for persistent stats

## License

MIT License

## Author

Rahul Mariyappagoudar
