EPSILON = 'epsilon'
THREE_STATES = ['q1', 'q2', 'q3']
FOUR_STATES = ['q1', 'q2', 'q3', 'q4']
SIX_STATES = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']
BINARY_ALPHABET = ['0', '1']
UNARY_ALPHABET = ['0']
AB_ALPHABET = ['a', 'b']

from NFA import NFA, test_nfa

# Example: NFA1
"""nfa1 accepts all inputs with strings that contain either 101 or 11 as a substring
"""
def transition_function(state, symbol):
    transition_dict = {
        ('q1', '0'): ('q1'),
        ('q1', '1'): ('q1', 'q2'),
        ('q1', EPSILON): (),
        ('q2', '0'): ('q3'),
        ('q2', '1'): (),
        ('q2', EPSILON): ('q3'),
        ('q3', '0'): (),
        ('q3', '1'): ('q4'),
        ('q3', EPSILON): (),
        ('q4', '0'): ('q4'),
        ('q4', '1'): ('q4'),
        ('q4', EPSILON): (),
    }
    return transition_dict.get((state, symbol))

nfa1 = NFA(FOUR_STATES, BINARY_ALPHABET, transition_function, FOUR_STATES[0], [FOUR_STATES[3]])
strings = ['010110', '00100']
print('nfa1: accepts all inputs with strings that contain either 101 or 11 as a substring')
test_nfa(nfa1, strings)


# NFA2
"""nfa2 accepts all inputs containing a 1 in the third position from the end
"""
def transition_function(state, symbol):
    transition_dict = {
        ('q1', '0'): ('q1'),
        ('q1', '1'): ('q1', 'q2'),
        ('q1', EPSILON): (),
        ('q2', '0'): ('q3'),
        ('q2', '1'): ('q3'),
        ('q2', EPSILON): (),
        ('q3', '0'): ('q4'),
        ('q3', '1'): ('q4'),
        ('q3', EPSILON): (),
        ('q4', '0'): (),
        ('q4', '1'): (),
        ('q4', EPSILON): (),

    }
    return transition_dict.get((state, symbol))

nfa2 = NFA(FOUR_STATES, BINARY_ALPHABET, transition_function, FOUR_STATES[0], [FOUR_STATES[3]])
strings = ['000100', '0011']
print('nfa2: accepts all inputs containing a 1 in the third position from the end')
test_nfa(nfa2, strings)


# NFA3
"""nfa3 accepts all inputs in the form 0 ** k where k is a multiple of 2 or 3
(note: superscript here denotes repetition, not numerical exponentiation)
"""
def transition_function(state, symbol):
    transition_dict = {
        ('q1', '0'): (),
        ('q1', EPSILON): ('q2', 'q4'),
        ('q2', '0'): ('q3'),
        ('q2', EPSILON): (),
        ('q3', '0'): ('q2'),
        ('q3', EPSILON): (),
        ('q4', '0'): ('q5'),
        ('q4', EPSILON): (),
        ('q5', '0'): ('q6'),
        ('q5', EPSILON): (),
        ('q6', '0'): ('q4'),
        ('q6', EPSILON): (),
    }
    return transition_dict.get((state, symbol))
nfa3 = NFA(SIX_STATES, UNARY_ALPHABET, transition_function, SIX_STATES[0], [SIX_STATES[1], SIX_STATES[3]])
strings = ['00', '000', '0000', '000000', '0', '00000']
print('nfa3: accepts all inputs where 0 is repeated multiple of 2 or multiple of 3 times')
test_nfa(nfa3, strings)


# NFA4
"""nfa4 accepts strings '', 'a', 'baba', 'baa', but it does not accept 'b', 'bb', 'babba'
"""
def transition_function(state, symbol):
    transition_dict = {
        ('q1', 'a'): (),
        ('q1', 'b'): ('q2'),
        ('q1', EPSILON): ('q3'),
        ('q2', 'a'): ('q2', 'q3'),
        ('q2', 'b'): ('q3'),
        ('q2', EPSILON): (),
        ('q3', 'a'): ('q1'),
        ('q3', 'b'): (),
        ('q3', EPSILON): (),
    }
    return transition_dict.get((state, symbol))
nfa4 = NFA(THREE_STATES, AB_ALPHABET, transition_function, THREE_STATES[0], [THREE_STATES[0]])
strings = ['', 'a', 'baba', 'baa', 'b', 'bb', 'babba']
print("nfa4: accepts strings '', 'a', 'baba', 'baa', but it does not accept 'b', 'bb', 'babba'")
test_nfa(nfa4, strings)