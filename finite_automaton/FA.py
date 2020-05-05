EPSILON = 'epsilon'

class FA:
    """Finite automaton"""
    def __init__(self, states, alphabet, transition_dict, start_state, accept_states):
        transition_keys = list(transition_dict.keys())
        assert all(len(key) == len(transition_keys[0]) for key in transition_keys), 'All keys in transition dictionary must be of the same length'
        assert start_state in states, 'Start state {0} not found in set of all possible states'.format(start_state)
        for f in accept_states:
            assert f in states, 'Accept state {0} not found in the set of all possible states'.format(f)
        self.states = states
        self.alphabet = alphabet
        self.transition_dict = transition_dict
        self.start_state = start_state
        self.accept_states = accept_states

    def compute(self, transition_input):
        return self.transition_dict.get(transition_input)

class DFA(FA):
    """Deterministic finite automaton"""
    def accept(self, string, verbose=False):
        current_state = self.start_state
        state_history = [self.start_state]
        for symbol in string:
            current_state = self.compute((current_state, symbol))
            state_history.append(current_state)
        if verbose:
            print(' '.join(state_history))
        return current_state in self.accept_states

class NFA(FA):
    """Nondeterministic finite automaton"""
    def epsilon_compute(self, states):
        next_states = states[:]
        for state in states:
            next_state = self.compute((state, EPSILON))
            if type(next_state) == tuple:
                next_states = next_states + list(next_state)
            elif type(next_state) == str:
                next_states.append(next_state)
        return next_states
    
    def nondeterministic_compute(self, states, symbol):
        next_states = []
        for state in states:
            next_state = self.compute((state, symbol))
            if type(next_state) == tuple:
                next_states = next_states + list(next_state)
            elif type(next_state) == str:
                next_states.append(next_state)
        return next_states

    def accept(self, string, verbose=False):
        current_states = [self.start_state]
        """Check if the start state has any epsilon arrows pointing out of it"""
        current_states = self.epsilon_compute(current_states)
        state_history = [current_states]
        for symbol in string:
            """Compute next state of each branch"""
            current_states = self.nondeterministic_compute(current_states, symbol)
            """Check if any of the new states has an epsilon arrow pointing out of it"""
            current_states = self.epsilon_compute(current_states)
            state_history.append(current_states)
        if verbose:
            for index, state_sequence in enumerate(state_history):
                print('i{0}: {1}'.format(index, ' '.join(state_sequence)))
        return any(state in self.accept_states for state in current_states)

