EPSILON = 'epsilon'

class NFA:
    """Nondeterministic finite automaton"""
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
        assert symbol in self.alphabet or symbol == EPSILON, 'Symbol {0} not recognized'.format(symbol)
        return self.transition_function(state, symbol)

    def accept(self, string, verbose=False):
        current_states = [self.start_state]
        state_history = [[self.start_state]]

        """Check if the start state has any epsilon arrows pointing out of it"""
        for current_state in current_states:
            epsilon_state = self.compute(current_state, EPSILON)
            if type(epsilon_state) == tuple:
                current_states = current_states + list(epsilon_state)
            elif type(epsilon_state) == str:
                current_states.append(epsilon_state)

        for symbol in string:
            next_states = []

            """Compute next state of each branch"""
            for current_state in current_states:
                next_state = self.compute(current_state, symbol)
                if type(next_state) == tuple:
                    next_states = next_states + list(next_state)
                elif type(next_state) == str:
                    next_states.append(next_state)

            """Check if any of the new states has an epsilon arrow pointing out of it"""
            for next_state in next_states:
                epsilon_state = self.compute(next_state, EPSILON)
                if type(epsilon_state) == tuple:
                    next_states = next_states + list(epsilon_state)
                elif type(epsilon_state) == str:
                    next_states.append(epsilon_state)

            current_states = next_states
            state_history.append(current_states)

        if verbose:
            for index, state_sequence in enumerate(state_history):
                print('i{0}: {1}'.format(index, ' '.join(state_sequence)))
                
        return any(state in self.accept_states for state in current_states)


def test_nfa(nfa, strings):
    for s in strings:
        print('{0} : {1}'.format(''.join(s), nfa.accept(s)))
    print()