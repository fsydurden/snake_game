# Snake Game 🐍

A classic Snake game implemented in Python using `pygame`. The game features smooth movement, score tracking, and collision detection.

### Game Demo

[![Watch the Snake Game Demo](./assets/snake_preview.gif)](./assets/snake_gif.mp4)


## 🚀 Installation & Setup

1. **Clone this repository**

   ```bash
   git clone https://github.com/fsydurden/snake_game.git
   cd snake_game
   ```

## ▶️ How to Play

Run the game:

```bash
python main.py
```

* Use **arrow keys** to move the snake
* Eat food to grow and increase your score
* Avoid hitting the walls or the snake's own body
* The game ends on collision; press **ESC** to exit

## 🧱 How it Works

* **`main.py`** controls the game loop and handles input
* **`snake.py`** manages snake movement and collision
* **`food.py`** spawns food randomly on the screen
* **`scorebord.py`** tracks and displays the score
