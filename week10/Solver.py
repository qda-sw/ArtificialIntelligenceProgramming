from Problem import *
from collections import deque
class Solver:
    def __init__(self, problem: Problem):
        self.problem = problem

    def breadth_first_search(self):
        # (state, actions, states)
        initial_state = self.problem.initial_state()
        frontier = deque()
        frontier.append((initial_state, [], [initial_state]))
        visited = set()
        visited.add(self.problem.hash_state(initial_state))
        #Implement your code
        while frontier:
            state, actions, states = frontier.popleft()
            if self.problem.goal_test(state):
                return states, actions
            for action in self.problem.actions(state):
                new_state = self.problem.result(state, action)
                if self.problem.hash_state(new_state) not in visited:
                    visited.add(self.problem.hash_state(new_state))
                    frontier.append((new_state, actions + [action], states + [new_state]))
        return None, None