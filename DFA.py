class DFA:
    """Deterministic finite automaton"""
    def __init__(self, states, alphabet, transition_dict, start_state, accept_states):
        assert start_state in states, 'Start state {0} not found in set of all possible states'.format(start_state)
        for f in accept_states:
            assert f in states, '{0} not found in the set of all possible states'.format(f)
        self.states = states
        self.alphabet = alphabet
        self.transition_dict = transition_dict
        self.start_state = start_state
        self.accept_states = accept_states
    def compute(self, state, symbol):
        assert symbol in self.alphabet, 'Symbol {0} not recognized'.format(symbol)
        return self.transition_dict.get((state, symbol))
    def accept(self, string, verbose=False):
        current_state = self.start_state
        state_history = [self.start_state]
        for symbol in string:
            current_state = self.compute(current_state, symbol)
            state_history.append(current_state)
        if verbose:
            print(' '.join(state_history))
        return current_state in self.accept_states

def test_dfa(dfa, strings):
    for s in strings:
        print('{0} : {1}'.format(''.join(s), dfa.accept(s)))
    print()