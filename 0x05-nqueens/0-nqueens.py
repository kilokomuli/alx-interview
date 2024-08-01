#!/usr/bin/env python3
"""solving N Queen problem using backtracking"""
import sys


def is_safe(board, row, col):
    """Check if the can be attacked vertically or diagonally"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve(N):
    """Checks if all queens are placed"""
    def place_queens(row):
        if row == N:
            solutions.append(board[:])
        else:
            for col in range(N):
                if is_safe(board, row, col):
                    board[row] = col
                    place_queens(row + 1)

    solutions = []
    board = [-1] * N
    place_queens(0)
    return solutions

def print_solutions(solutions, N):
    """Prints the solutions"""
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])

def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve(N)
    print_solutions(solutions, N)

if __name__ == "__main__":
    main()