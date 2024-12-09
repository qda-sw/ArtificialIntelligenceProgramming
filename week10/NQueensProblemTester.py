import random
from NQueensProblem import *
from Solver import *

def main():
    n = 8
    # Randomly place a queen in the first column
    first_row = random.randint(0, n - 1)
    initial_state = (first_row,)

    # There are no queens on the board.
    #initial_state = ()
    problem = NQueensProblem(n, initial_state)
    solver = Solver(problem)
    state_sequence, action_sequence = solver.breadth_first_search()
    if state_sequence is None:
        print("No solution found.")
        return

    #print(f"Initial state with queen at column 0, row {first_row}:")
    print_state(state_sequence[0], n)
    for idx in range(1, len(state_sequence)):
        print(f"After placing queen in column {idx}:")
        print_state(state_sequence[idx], n)


def print_state(state, n):
    for row in range(n):
        line = ""
        for col in range(n):
            if col < len(state) and state[col] == row:
                line += "Q "
            else:
                line += "x "
        print(line)
    print()

if __name__ == "__main__":
    main()
