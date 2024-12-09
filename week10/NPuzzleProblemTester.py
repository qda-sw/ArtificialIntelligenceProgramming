from Solver import Solver
from NPuzzleProblem import NPuzzleProblem

def main():
    n = 3
    problem = NPuzzleProblem(n)
    solver = Solver(problem)
    state_sequence, action_sequence = solver.breadth_first_search()
    if state_sequence is None:
        print("No solution found.")
        return

    print("Initial State:")
    print_state(state_sequence[0], n)
    for idx, action in enumerate(action_sequence[:]):
        print(f"Action: {action}")
        print_state(state_sequence[idx + 1], n)



def print_state(state, n):
    for i in range(n):
        print(state[i * n:(i + 1) * n])
    print()


if __name__ == "__main__":
    main()