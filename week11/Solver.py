from abc import ABC, abstractmethod
from typing import Any
from Problem import Problem

class Solver(ABC):
    def __init__(self, problem: Problem):
        self.problem = problem
        # Logging the value of the objective function
        self.progress = []

    @abstractmethod
    def solve(self):
        pass

    def track_progress(self, state: Any):
        score = self.problem.objective_function(state)
        self.progress.append(score)