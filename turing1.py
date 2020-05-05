BLANK_SYMBOL = '[]'
Q_ACCEPT = 'q_accept'
Q_REJECT = 'q_reject'
LEFT = 'left'
RIGHT = 'right'

from TuringMachine import TuringMachine

description = 'This Turing Machine decides the language A = { w | w = 0 ** 2 ** n where n >= 0 }'
states = ['q1', 'q2', 'q3', 'q4', 'q5', Q_ACCEPT, Q_REJECT]
input_alphabet = ['0']
tape_alphabet = ['0', 'x', BLANK_SYMBOL]
start_state = 'q1'
accept_state = Q_ACCEPT
reject_state = Q_REJECT
transition_function = {
    ('q1', '0'): ('q2', BLANK_SYMBOL, RIGHT),
    ('q1', 'x'): (Q_REJECT, 'x', RIGHT),
    ('q1', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q2', '0'): ('q3', 'x', RIGHT),
    ('q2', 'x'): ('q2', 'x', RIGHT),
    ('q2', BLANK_SYMBOL): (Q_ACCEPT, BLANK_SYMBOL, RIGHT),
    ('q3', '0'): ('q4', '0', RIGHT),
    ('q3', 'x'): ('q3', 'x', RIGHT),
    ('q3', BLANK_SYMBOL): ('q5', BLANK_SYMBOL, LEFT),
    ('q4', '0'): ('q3', 'x', RIGHT),
    ('q4', 'x'): ('q4', 'x', RIGHT),
    ('q4', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q5', '0'): ('q5', '0', LEFT),
    ('q5', 'x'): ('q5', 'x', LEFT),
    ('q5', BLANK_SYMBOL): ('q2', BLANK_SYMBOL, RIGHT)
}

tm1 = TuringMachine(
    states, 
    input_alphabet, 
    tape_alphabet, 
    transition_function, 
    start_state, 
    accept_state, 
    reject_state, 
    description)
