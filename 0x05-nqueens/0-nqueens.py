import sys

def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper diagonal on right side
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, row, N, solutions):
    if row == N:
        solutions.append([[i, col] for i, col in enumerate(board)])
        return
    
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, N, solutions)
            board[row][col] = 0

def solve_n_queens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    
    for sol in solutions:
        print(sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    solve_n_queens(sys.argv[1])
