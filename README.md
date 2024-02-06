# Pygame Pong Game

This project is a simple implementation of the classic Pong game using Python and the Pygame library. The game features a single player mode where the player controls a paddle to hit a ball back and forth. The goal is to keep the ball from passing your paddle, with the game keeping track of the number of successful hits as your score. The game ends when the ball passes the paddle.

## Features

- Basic Pong gameplay mechanics
- Score tracking
- Game over condition when the ball passes the paddle

## Requirements

To run this game, you'll need:

- Python 3.x
- Pygame library

## Installation

First, ensure you have Python installed on your system. If you don't have Python installed, download and install it from [python.org](https://www.python.org/downloads/).

Next, install Pygame. Open your terminal or command prompt and run the following command: `pip install pygame`


## Running the Game

To start the game, navigate to the game's directory in your terminal or command prompt and run: python pong.py
Replace `pong.py` with the actual name of your Python script if it's different. You may also have to replace `python` with `python3` depending what python you have installed

## How to Play

- Use the left and right arrow keys to move the paddle.
- Try to hit the ball with the paddle to keep it from passing by.
- The game tracks the number of times you successfully hit the ball as your score.
- The game ends when the ball passes the paddle, displaying your final score.

## Code Explanation

- **Pygame Initialization**: The game starts by initializing Pygame and setting up the game window with a specific size.
- **Game Variables**: Variables are defined for the paddle and ball positions, speed, and the game score.
- **Paddle Movement**: The game listens for key presses and releases to move the paddle left or right, ensuring it stays within the screen bounds.
- **Ball Movement**: The ball moves according to its speed, bouncing off the walls and the paddle. The score increments with each successful hit.
- **Game Over**: The game ends when the ball passes the paddle, printing the final score and exiting.

## Pygame Utilization

Throughout the game, Pygame is used for:

- Creating and managing the game window.
- Handling events like keyboard inputs.
- Drawing shapes (the paddle and ball) and text (the score) on the screen.
- Managing game frames and updating the display.

## Contributing

Feel free to fork this project, make changes, and submit pull requests if you have ideas for improvements or bug fixes.

## License

This project is open source and available under the [MIT License](LICENSE.md).





