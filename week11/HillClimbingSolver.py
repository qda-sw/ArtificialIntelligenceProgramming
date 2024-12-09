from typing import Any, List
from Solver import Solver
import numpy as np

class HillClimbingSolver(Solver):
    def __init__(self, problem):
        super().__init__(problem)
        self.problem = problem
    def solve(self) -> Any:
        current = self.problem.initial_state()
        for i in range(1000):
            super().track_progress(current)
            neighbors = self._generate_neighbors(current)
            next_state = self._select_next_state(current, neighbors)
            if self.problem.objective_function(next_state) > self.problem.objective_function(current):
                return current
            current = next_state
        return current
    def _generate_neighbors(self, current_state: Any) -> List[Any]:
        return [self.problem.result(current_state, action) for action in self.problem.actions(current_state)]

    def _select_next_state(self, current_state: Any, neighbors: List[Any]) -> Any:
        return max(neighbors, key=lambda state: self.problem.objective_function(state))