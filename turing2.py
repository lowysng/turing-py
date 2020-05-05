BLANK_SYMBOL = '[]'
Q_ACCEPT = 'q_accept'
Q_REJECT = 'q_reject'
LEFT = 'left'
RIGHT = 'right'

from TuringMachine import TuringMachine
from util import get_states

# This Turing Machine decides the language B = { w#w | w = {0, 1}* }

states = get_states(8) + [Q_ACCEPT, Q_REJECT]
input_alphabet = ['0', '1', '#']
tape_alphabet = ['0', '1', '#', 'x', BLANK_SYMBOL]
start_state = 'q1'
accept_state = Q_ACCEPT
reject_state = Q_REJECT
transition_function = {
    ('q1', '0'): ('q2', 'x', RIGHT),
    ('q1', '1'): ('q3', 'x', RIGHT),
    ('q1', '#'): ('q8', '#', RIGHT),
    ('q1', 'x'): (Q_REJECT, 'x', RIGHT),
    ('q1', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q2', '0'): ('q2', '0', RIGHT),
    ('q2', '1'): ('q2', '1', RIGHT),
    ('q2', '#'): ('q4', '#', RIGHT),
    ('q2', 'x'): (Q_REJECT, 'x', RIGHT),
    ('q2', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q3', '0'): ('q3', '0', RIGHT),
    ('q3', '1'): ('q3', '1', RIGHT),
    ('q3', '#'): ('q5', '#', RIGHT),
    ('q3', 'x'): (Q_REJECT, 'x', RIGHT),
    ('q3', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q4', '0'): ('q6', 'x', LEFT),
    ('q4', '1'): (Q_REJECT, '1', RIGHT),
    ('q4', '#'): (Q_REJECT, '#', RIGHT),
    ('q4', 'x'): ('q4', 'x', RIGHT),
    ('q4', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q5', '0'): (Q_REJECT, '0', RIGHT),
    ('q5', '1'): ('q6', 'x', LEFT),
    ('q5', '#'): (Q_REJECT, '#', RIGHT),
    ('q5', 'x'): ('q5', 'x', RIGHT),
    ('q5', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q6', '0'): ('q6', '0', LEFT),
    ('q6', '1'): ('q6', '1', LEFT),
    ('q6', '#'): ('q7', '#', LEFT),
    ('q6', 'x'): ('q6', 'x', LEFT),
    ('q6', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q7', '0'): ('q7', '0', LEFT),
    ('q7', '1'): ('q7', '1', LEFT),
    ('q7', '#'): (Q_REJECT, '#', RIGHT),
    ('q7', 'x'): ('q1', 'x', RIGHT),
    ('q7', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q8', '0'): (Q_REJECT, '0', RIGHT),
    ('q8', '1'): (Q_REJECT, '1', RIGHT),
    ('q8', '#'): (Q_REJECT, '#', RIGHT),
    ('q8', 'x'): ('q8', 'x', RIGHT),
    ('q8', BLANK_SYMBOL): (Q_ACCEPT, BLANK_SYMBOL, RIGHT),
}

tm2 = TuringMachine(states, input_alphabet, tape_alphabet, transition_function, start_state, accept_state, reject_state)