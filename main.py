import math
import time




HUMAN = 'O'
AI = 'X'
EMPTY = ' '
board = [[EMPTY for _ in range(3)] for _ in range(3)]
def print_board(b):
    print("\nCurrent board:")
    for row in b:
        print(' | '.join(row))
        print('--' * 5)
def check_winner(b):

    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != EMPTY:
            return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != EMPTY:
            return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] != EMPTY:
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != EMPTY:
        return b[0][2]
    return None
def is_draw(b):
    for row in b:
        if EMPTY in row:
            return False
    return check_winner(b) is None
def minimax(b, depth, is_maximizing):
    winner = check_winner(b)
    if winner == AI:
        return 10 - depth
    elif winner == HUMAN:
        return depth - 10
    elif is_draw(b):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = AI
                    score = minimax(b, depth + 1, False)
                    b[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = HUMAN
                    score = minimax(b, depth + 1, True)
                    b[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score
def best_move(b):
    best_score = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if b[i][j] == EMPTY:
                b[i][j] = AI
                score = minimax(b, 0, False)
                b[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move
def human_turn(b):
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter col (0, 1, or 2): "))
            if b[row][col] == EMPTY:
                b[row][col] = HUMAN
                break
            else:
                print("Cell already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Enter numbers from 0 to 2.")
print(" Tic-Tac-Toe!")
print_board(board)
while True:
    human_turn(board)
    print_board(board)

    if check_winner(board):
        print(f"\n{check_winner(board)} wins!")
        break
    if is_draw(board):
        print("\nIt's a draw!")
        break


    print("AI is thinking...")
    i, j = best_move(board)
    board[i][j] = AI
    print_board(board)

    if check_winner(board):
        print(f"\n{check_winner(board)} wins!")
        break
    if is_draw(board):
        print("\nIt's a draw!")
        break


#question2

stats = {
    "nodes": 0,
    "depth": 0,
    "start_time": 0,
    "end_time": 0
}
def print_board(b):
    print("\nCurrent Board:")
    for row in b:
        print(' | '.join(row))
        print('--' * 5)
def check_winner(b):
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] != EMPTY:
            return b[i][0]
        if b[0][i] == b[1][i] == b[2][i] != EMPTY:
            return b[0][i]
    if b[0][0] == b[1][1] == b[2][2] != EMPTY:
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != EMPTY:
        return b[0][2]
    return None
def is_draw(b):
    for row in b:
        if EMPTY in row:
            return False
    return check_winner(b) is None
def reset_stats():
    stats["nodes"] = 0
    stats["depth"] = 0
    stats["start_time"] = 0
    stats["end_time"] = 0
# Minimax with Alpha-Beta Pruning
def alphabeta(b, depth, alpha, beta, is_max):
    stats["nodes"] += 1
    stats["depth"] = max(stats["depth"], depth)

    winner = check_winner(b)
    if winner == AI:
        return 10 - depth
    elif winner == HUMAN:
        return depth - 10
    elif is_draw(b):
        return 0

    if is_max:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = AI
                    score = alphabeta(b, depth + 1, alpha, beta, False)
                    b[i][j] = EMPTY
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if b[i][j] == EMPTY:
                    b[i][j] = HUMAN
                    score = alphabeta(b, depth + 1, alpha, beta, True)
                    b[i][j] = EMPTY
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score
def best_move(b):
    best_score = -math.inf
    move = (-1, -1)
    reset_stats()
    stats["start_time"] = time.time()

    for i in range(3):
        for j in range(3):
            if b[i][j] == EMPTY:
                b[i][j] = AI
                score = alphabeta(b, 0, -math.inf, math.inf, False)
                b[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)

    stats["end_time"] = time.time()
    return move
def human_turn(b):
    while True:
        try:
            row = int(input("Enter your move row (0, 1, 2): "))
            col = int(input("Enter your move col (0, 1, 2): "))
            if 0 <= row < 3 and 0 <= col < 3 and b[row][col] == EMPTY:
                b[row][col] = HUMAN
                break
            else:
                print("Invalid or occupied cell. Try again.")
        except ValueError:
            print("Please enter valid numbers (0-2).")
def print_ai_stats():
    print("\nAI Turn Stats:")
    print(f"Nodes explored: {stats['nodes']}")
    print(f"Max depth reached: {stats['depth']}")
    print(f"Execution time: {stats['end_time'] - stats['start_time']:.6f} seconds")
    print("   ")
print("Tic-Tac-Toe! ")
print_board(board)
while True:

    human_turn(board)
    print_board(board)

    if check_winner(board):
        print(f"\n{check_winner(board)} wins!")
        break
    if is_draw(board):
        print("\nIt's a draw!")
        break
    print("AI is thinking...")
    i, j = best_move(board)

    board[i][j] = AI
    print_board(board)
    print(f"AI moved to ({i}, {j})")
    print_ai_stats()

    if check_winner(board):
        print(f"\n{check_winner(board)} wins!")
        break
    if is_draw(board):
        print("\nIt's a draw!")
        break




