from Solver import Solver
from HillClimbingSolver import HillClimbingSolver
class RandomRestartHillCLimbingSolver(Solver):
    def __init__(self, problem):
        super().__init__(problem)
        self.problem = problem
        self.max_restarts = 100000
    def solve(self):
        best_state = self.problem.initial_state()
        best_score = self.problem.objective_function(best_state)
        solver = HillClimbingSolver(self.problem)
        for _ in range(self.max_restarts):
            state = solver.solve()
            score = self.problem.objective_function(state)
            super().track_progress(state)
            if score < best_score:
                best_state = state
                best_score = score
            if self.problem.goal_test(state):
                return state
        return best_state