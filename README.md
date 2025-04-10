# 🤖 Tic-Tac-Toe AI using Minimax and Alpha-Beta Pruning

This project implements a smart AI for the classic **Tic-Tac-Toe** game using the **Minimax algorithm** and its optimized version with **Alpha-Beta Pruning**. The AI plays optimally against a human and ensures the best possible outcome.

---

## 🎮 Game Rules

1. The game is played on a 3x3 grid.
2. Players take turns placing their symbol (X or O) on the board.
3. The player who first aligns three of their symbols horizontally, vertically, or diagonally wins.
4. If all spaces are filled and no player has won, the game ends in a draw.

---

## 🧠 AI Implementation

### ✅ Phase 1: Minimax Algorithm

- The AI uses a recursive **Minimax function** to evaluate all possible game states.
- Assigns scores:  
  - Win = +1  
  - Lose = -1  
  - Draw = 0
- Picks the move that maximizes the AI's chances of winning and minimizes the opponent's.

### 🧠 Phase 2: Alpha-Beta Pruning Optimization

- Improves Minimax by eliminating unnecessary branches (prunes unpromising moves).
- This reduces the number of nodes explored and significantly **improves performance**.
- Ensures optimal play but with reduced computation time.

---

## 📊 Performance Comparison

The project compares **Minimax vs Alpha-Beta Pruning** on three metrics:

| Metric                | Minimax | Alpha-Beta Pruning |
|-----------------------|---------|--------------------|
| Nodes Explored        | High    | Reduced            |
| Execution Time        | Slower  | Faster             |
| Max Search Depth      | Same    | Same (but faster)  |

> These values are printed dynamically during execution for analysis.

---

## ✅ Requirements

- Python 3.7+
- No external dependencies (standard library only)

---

## 🚀 How to Run

```bash
git clone https://github.com/your-username/tic-tac-toe-ai-minimax.git
cd tic-tac-toe-ai-minimax
python main.py
