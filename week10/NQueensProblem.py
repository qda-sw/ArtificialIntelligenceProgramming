from Problem import *
class NQueensProblem(Problem):
    def __init__(self, n: int, initial_state: Tuple[int, ...] = None):
        self.n = n
        if initial_state is not None:
            self.initial = initial_state
        else:
            self.initial = tuple()

    def initial_state(self) -> Tuple[int, ...]:
        return self.initial

    def actions(self, state: Tuple[int, ...]) -> List[int]:
        valid_actions = []
        #Implement your code
        for action in range(self.n):
            next_state = self.result(state, action)
            if self.is_valid(next_state):
                valid_actions.append(action)
        return valid_actions

    def hash_state(self, state: Tuple[int, ...]) -> int:
        return hash(state)

    def is_valid(self, state: Tuple[int, ...]) -> bool:
        current_col = len(state) - 1
        #Implement your code
        current_row = state[current_col]
        for col in range(current_col-1, -1, -1):
            row = state[col]
            if row == current_row or abs(row - current_row) == current_col - col:
                return False
        return True

    def result(self, state: Tuple[int, ...], action: int) -> Tuple[int, ...]:
        return state + (action,)

    def goal_test(self, state: Tuple[int, ...]) -> bool:
        return len(state) == self.n and self.is_valid(state)

    def step_cost(self, state: Tuple[int, ...], action: int) -> float:
        return 1