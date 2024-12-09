import random
from typing import List, Tuple, Any
from Problem import Problem
from HillClimbingSolver import *
from RandomRestartHillClimbingSolver import *
from NQueensProblem import NQueensProblem
def main():
    n = 8
    problem = NQueensProblem(n)
    solver = RandomRestartHillCLimbingSolver(problem)

    solution = solver.solve()   

    if solution is None or not problem.goal_test(solution):
        print("No solution found or local optimum reached. Final board configuration:")
        print_board(solution, n)
        print("Objective Value:", problem.objective_function(solution))
    else:
        print("Solution found:")
        print_board(solution, n)
        print("Objective Value Progress:", solver.progress)

def print_board(state: List[int], n: int):
    for row in range(n):
        line = ""
        for col in range(n):
            if state[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

if __name__ == "__main__":
    main()