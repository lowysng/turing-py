BLANK_SYMBOL = '[]'
Q_ACCEPT = 'q_accept'
Q_REJECT = 'q_reject'
LEFT = 'left'
RIGHT = 'right'

from TuringMachine import TuringMachine

# This Turing Machine decides the language A = { w | w contains an equal number of 0s and 1s }

states = ['q1', 'q2', 'q3', 'q4', 'q5', Q_ACCEPT, Q_REJECT]
input_alphabet = ['0', '1']
tape_alphabet = ['0', '1', 'x', BLANK_SYMBOL]
start_state = 'q1'
accept_state = Q_ACCEPT
reject_state = Q_REJECT
transition_function = {
    ('q1', '0'): ('q2', BLANK_SYMBOL, RIGHT),
    ('q1', '1'): ('q3', BLANK_SYMBOL, RIGHT),
    ('q2', '0'): ('q2', '0', RIGHT),
    ('q2', '1'): ('q4', 'x', LEFT),
    ('q2', 'x'): ('q2', 'x', RIGHT),
    ('q2', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q3', '0'): ('q4', 'x', LEFT),
    ('q3', '1'): ('q3', '1', RIGHT),
    ('q3', 'x'): ('q3', 'x', RIGHT),
    ('q3', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q4', '0'): ('q4', '0', LEFT),
    ('q4', '1'): ('q4', '1', LEFT),
    ('q4', 'x'): ('q4', 'x', LEFT),
    ('q4', BLANK_SYMBOL): ('q5', BLANK_SYMBOL, RIGHT),
    ('q5', '0'): ('q2', 'x', RIGHT),
    ('q5', '1'): ('q3', 'x', RIGHT),
    ('q5', 'x'): ('q5', 'x', RIGHT),
    ('q5', BLANK_SYMBOL): (Q_ACCEPT, BLANK_SYMBOL, RIGHT)
}

tm4 = TuringMachine(states, input_alphabet, tape_alphabet, transition_function, start_state, accept_state, reject_state)
