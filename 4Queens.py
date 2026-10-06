print("Dharmik Bosamia")
print("53013240021")
def solve_n_queens(n):
    def backtrack(r):
        if r == n: return True  # All queens placed successfully
        for c in range(n):
            # Check if column or diagonals are already attacked
            if c in cols or (r - c) in diag1 or (r + c) in diag2: continue
            
            cols.add(c); diag1.add(r - c); diag2.add(r + c); board[r][c] = 1
            if backtrack(r + 1): return True  # Move to next row
            cols.remove(c); diag1.remove(r - c); diag2.remove(r + c); board[r][c] = 0
        return False

    board = [[0] * n for _ in range(n)]
    cols, diag1, diag2 = set(), set(), set()
    
    if backtrack(0):
        for row in board: print(*row)  # Prints grid neatly
    else:
        print("No solution exists")

# Example Usage
n = int(input("Enter chessboard size (N): "))
solve_n_queens(n)
