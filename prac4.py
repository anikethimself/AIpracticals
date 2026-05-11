def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i] == j:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i] == j:
            return False

    return True

def solve_nqueens(board, row, n):
    if row == n:
        print("\nSolution:")
        for i in range(n):
            for j in range(n):
                if board[i] == j:
                    print("Q", end=" ")
                else:
                    print(".", end=" ")
            print()
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col   # place queen

            if solve_nqueens(board, row + 1, n):
                return True

            board[row] = -1    # backtrack

    return False


n = int(input("Enter number of queens: "))

board = [-1] * n

if not solve_nqueens(board, 0, n):
    print("No solution exists")