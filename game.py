import math

def create_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)


def check_winner(board, player):
    
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
    
    # check columns
    for col in range(3):
        if  board[0][col] == board[1][col] == board[2][col] == player:
            return True 
    
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        True
    if board[0][2] == board[1][1] == board[2][0] == player:
        True

    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False 
    return True

def minimax(board, depth, is_maximizing):

    """
    Implement the Minimax algorithm to determine the best move for the AI in the tic tac to game.

    Parameters:
    - board: list[list[str]]: The current state of the game board.
    - depth: int: The current depth in the seearch tree.
    - is_maximizing: bool: A boolean indicator indicating whether it's the turn of the player whor wants to maximize their score (True) or the player who wants to minimize it (False).

    Retunrs: 
    - int: The score associated with the current state of the board 
    """

    # If there's a winner: return 1 if AI wins, -1  if human player wins 
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if check_draw(board):
        return 0 
    
     # If it's the turn of the player who wants to maximize their score
    if is_maximizing:
        best_score = -math.inf # Initialize the best score as negative infinity 
        
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O' # Try the move for the AI
                    score = minimax(board, depth + 1, False) # Recursivily call minimax to evaluate the next move for the human player 
                    board[i][j] = ' ' # Undo the move
                    best_score = max (score, best_score) #Update the best score 
        return best_score
    
    else:
        best_score = math.inf # Initialize the best score as infinity 

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X' # Try the move for the human player
                    score = minimax(board, depth + 1, True)  # Recursively call minimax to evaluate the next move for the AI
                    board[i][j] = ' '
                    best_score = min(score, best_score) # Update the best score
        
        return best_score

def game():
    board = [[" " for _ in range(3)] for _ in range(3)]



