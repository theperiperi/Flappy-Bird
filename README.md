# Flappy Bird Game

This is a simple implementation of the classic Flappy Bird game using Python and Pygame.## Demo

## How to Play

### Objective
The objective of the game is to navigate the bird through a series of pipes without hitting them. Each pipe passed gives the player a point. The game ends when the bird collides with a pipe or the ground.

### Controls
- Press the `SPACEBAR` to make the bird flap and fly upward.
- After game over, press `ENTER` to play again.

## Installation

1. Make sure you have Python installed. You can download it [here](https://www.python.org/downloads/).
2. Clone this repository to your local machine:

  git clone https://github.com/theperiperi/flappy-bird.git

3. Install the required dependencies using pip:
```bash
pip install pygame
```

   
## How to Run

Navigate to the project directory in your terminal and run the following command:

```bash
python main.py
```

## Game Features

- **Scoring**: Each pipe passed earns the player 10 points. A sound plays when the player reaches a multiple of 100 points.
- **High Score**: The game keeps track of the highest score achieved.
- **Sound Effects**: Flap sound when the bird jumps, hit sound when the bird collides with a pipe, and point sound when points are scored.
- **Responsive Design**: The game adjusts to the screen size of 400x600 pixels.
- **Restart**: After a game over, players can press `ENTER` to play again.

## File Structure

- `main.py`: Contains the main game loop and logic.
- `sprites.py`: Defines the Bird and Pipe classes.
- `soundboard.py`: Manages the game's sound effects.
- `sprites`: Contains images used for the bird and pipes.
- `README.md`: The file you are currently reading, providing information about the game.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.



![image](https://github.com/theperiperi/Flappy-Bird/assets/121922820/37b92e82-af62-4303-8bd1-5fd76dc14cc5)
