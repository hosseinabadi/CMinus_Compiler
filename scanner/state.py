class State:
    def __init__(self):
        self.next_states = []

    def add_next_state(self, interval, next_state):
        self.next_states.append([interval, next_state])


class FinalState(State):
    def __init__(self, backward):
        super.__init__()
        self.backward = backward

