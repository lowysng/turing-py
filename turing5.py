BLANK_SYMBOL = '[]'
Q_ACCEPT = 'q_accept'
Q_REJECT = 'q_reject'
LEFT = 'left'
RIGHT = 'right'

from TuringMachine import TuringMachine
from util import get_states

description = 'This Turing Machine decides the language { w | w contains twice as many 0s as 1s }'
states = get_states(8) + [Q_ACCEPT, Q_REJECT]
input_alphabet = ['0', '1']
tape_alphabet = ['0', '1', 'x', BLANK_SYMBOL]
start_state = 'q1'
accept_state = Q_ACCEPT
reject_state = Q_REJECT
transition_function = {
    ('q1', '0'): ('q2', BLANK_SYMBOL, RIGHT),
    ('q1', '1'): ('q5', BLANK_SYMBOL, RIGHT),
    ('q2', '0'): ('q3', 'x', RIGHT),
    ('q2', '1'): ('q4', 'x', RIGHT),
    ('q2', 'x'): ('q2', 'x', RIGHT),
    ('q2', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q3', '0'): ('q3', '0', RIGHT),
    ('q3', '1'): ('q7', 'x', LEFT),
    ('q3', 'x'): ('q3', 'x', RIGHT),
    ('q3', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q4', '0'): ('q7', 'x', LEFT),
    ('q4', '1'): ('q4', '1', RIGHT),
    ('q4', 'x'): ('q4', 'x', RIGHT),
    ('q4', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q5', '0'): ('q6', 'x', RIGHT),
    ('q5', '1'): ('q5', '1', RIGHT),
    ('q5', 'x'): ('q5', 'x', RIGHT),
    ('q5', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q6', '0'): ('q7', 'x', LEFT),
    ('q6', '1'): ('q6', '1', RIGHT),
    ('q6', 'x'): ('q6', 'x', RIGHT),
    ('q6', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q7', '0'): ('q7', '0', LEFT),
    ('q7', '1'): ('q7', '1', LEFT),
    ('q7', 'x'): ('q7', 'x', LEFT),
    ('q7', BLANK_SYMBOL): ('q8', BLANK_SYMBOL, RIGHT),
    ('q8', '0'): ('q2', 'x', RIGHT),
    ('q8', '1'): ('q5', 'x', RIGHT),
    ('q8', 'x'): ('q8', 'x', RIGHT),
    ('q8', BLANK_SYMBOL): (Q_ACCEPT, BLANK_SYMBOL, RIGHT),
}

tm5 = TuringMachine(
    states, 
    input_alphabet, 
    tape_alphabet, 
    transition_function,
    start_state, 
    accept_state, 
    reject_state,
    description)