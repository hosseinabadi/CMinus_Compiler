from scanner.state import State, FinalState
from scanner.interval import Interval


class Regex:
    def __init__(self):
        state_zero = State()
        self.states = [state_zero]
        self.number()
        self.ID_keyword()
        self.whitespace()
        self.symbol()
        self.comment()

    def number(self):
        state1 = State()
        state2 = FinalState(True)
        self.state_zero.add_next_state(Interval.contain("0", "9"), state1)
        self.state1.add_next_state(Interval.contain("0", "9"), state1)
        interval_state1 = Interval
        interval_state1.expect("a", "z")
        interval_state1.expect("A", "Z")
        interval_state1.expect("0", "9")
        self.state1.add_next_state(interval_state1, state2)
        self.states.append(state1, state2)

    def ID_keyword(self):
        ...

    def symbol(self):
        ...

    def comment(self):
        ...

    def whitespace(self):
        ...
