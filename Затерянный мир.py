def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True


def solve(board, row, n, result):
    if row == n:
        return result + 1

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            result = solve(board, row + 1, n, result)
            board[row][col] = 0
    return result


def solve_n(n):
    result = 0
    board = [[0 for _ in range(n)] for _ in range(n)]
    result = solve(board, 0, n, result)
    return result


n = int(input())
solutions = solve_n(n)
print(solutions)

