class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]  # Initialize empty n x n board
        self.solutions = []  # List to store valid solutions

    def is_safe(self, row, col):
        # Check if it's safe to place a queen at board[row][col]
        # Check the row
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check the upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        # Check the lower diagonal on left side
        for i, j in zip(range(row, self.n, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve_backtracking(self, col):
        # Base case: If all queens are placed, append the current board configuration to solutions
        if col == self.n:
            self.solutions.append([row[:] for row in self.board])
            return True

        for row in range(self.n):
            if self.is_safe(row, col):
                # Place the queen
                self.board[row][col] = 1

                # Recur to place the rest of the queens
                self.solve_backtracking(col + 1)

                # Backtrack
                self.board[row][col] = 0

        return False

    def solve_branch_and_bound(self, col):
        # Base case: If all queens are placed, append the current board configuration to solutions
        if col == self.n:
            self.solutions.append([row[:] for row in self.board])
            return True

        for row in range(self.n):
            if self.is_safe(row, col):
                # Place the queen
                self.board[row][col] = 1

                # Check if adding this queen leads to a valid solution
                if self.solve_branch_and_bound(col + 1):
                    return True

                # Backtrack
                self.board[row][col] = 0

        return False

    def find_solutions_backtracking(self):
        # Start solving using backtracking from the first column (col=0)
        self.solve_backtracking(0)
        return self.solutions

    def find_solutions_branch_and_bound(self):
        # Start solving using branch and bound from the first column (col=0)
        self.solve_branch_and_bound(0)
        return self.solutions

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))
    print()

def main():
    n = 4 # Specify the size of the chessboard and number of queens

    # Solve the n-queens problem using backtracking
    n_queens_backtracking = NQueens(n)
    solutions_backtracking = n_queens_backtracking.find_solutions_backtracking()

    print(f"Total solutions found using backtracking: {len(solutions_backtracking)}")
    for i, solution in enumerate(solutions_backtracking):
        print(f"Solution {i + 1}:")
        print_board(solution)

    # Solve the n-queens problem using branch and bound
    n_queens_branch_bound = NQueens(n)
    solutions_branch_bound = n_queens_branch_bound.find_solutions_branch_and_bound()

    print(f"Total solutions found using branch and bound: {len(solutions_branch_bound)}")
    for i, solution in enumerate(solutions_branch_bound):
        print(f"Solution {i + 1}:")
        print_board(solution)

if __name__ == "__main__":
    main()
