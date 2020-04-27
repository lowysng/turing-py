class DFA:
    """Deterministic finite automaton"""
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        assert start_state in states, 'Start state {0} not found in set of all possible states'.format(start_state)
        for f in accept_states:
            assert f in states, '{0} not found in the set of all possible states'.format(f)
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.start_state = start_state
        self.accept_states = accept_states
    def compute(self, state, symbol):
        assert symbol in self.alphabet, 'Symbol {0} not recognized'.format(symbol)
        return self.transition_function(state, symbol)
    def accept(self, string, verbose=False):
        current_state = self.start_state
        state_history = [self.start_state]
        for symbol in string:
            current_state = self.compute(current_state, symbol)
            state_history.append(current_state)
        if verbose:
            print(' '.join(state_history))
        return current_state in self.accept_states

states = ['q1', 'q2', 'q3']
alphabet = ['0', '1']
def transition_function(state, symbol):
    transition_dict = {
        ('q1', '0'): 'q1',
        ('q1', '1'): 'q2',
        ('q2', '1'): 'q2',
        ('q2', '0'): 'q3',
        ('q3', '0'): 'q2',
        ('q3', '1'): 'q2'}
    return transition_dict.get((state, symbol))
start_state = states[0]
accept_states = [states[1]]

dfa = DFA(states, alphabet, transition_function, start_state, accept_states)
print(dfa.accept('100100', verbose=True))