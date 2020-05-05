BLANK_SYMBOL = '[]'
Q_ACCEPT = 'q_accept'
Q_REJECT = 'q_reject'
LEFT = 'left'
RIGHT = 'right'

from TuringMachine import TuringMachine
from util import get_states

# This Turing Machine decides the language C = { (a**i)(b**j)(c**k) | i * j = k and i, j, k >= 1 }

states = get_states(8) + [Q_ACCEPT, Q_REJECT]
input_alphabet = ['a', 'b', 'c']
tape_alphabet = ['a', 'b', 'c', 'A', 'B', 'C', BLANK_SYMBOL]
start_state = 'q1'
accept_state = Q_ACCEPT
reject_state = Q_REJECT
transition_function = {
    ('q1', 'a'): ('q2', BLANK_SYMBOL, RIGHT),
    ('q1', 'b'): (Q_REJECT, 'b', RIGHT),
    ('q1', 'c'): (Q_REJECT, 'c', RIGHT),
    ('q1', 'x'): (Q_REJECT, 'x', RIGHT),
    ('q1', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q2', 'a'): ('q2', 'a', RIGHT),
    ('q2', 'b'): ('q3', 'b', RIGHT),
    ('q2', 'c'): (Q_REJECT, 'c', RIGHT),
    ('q2', 'x'): (Q_REJECT, 'x', RIGHT),
    ('q2', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q3', 'a'): (Q_REJECT, 'a', RIGHT),
    ('q3', 'b'): ('q3', 'b', RIGHT),
    ('q3', 'c'): ('q4', 'c', RIGHT),
    ('q3', 'x'): (Q_REJECT, 'x', RIGHT),
    ('q3', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q4', 'a'): (Q_REJECT, 'a', RIGHT),
    ('q4', 'b'): (Q_REJECT, 'b', RIGHT),
    ('q4', 'c'): ('q4', 'c', RIGHT),
    ('q4', 'x'): (Q_REJECT, 'x', RIGHT),
    ('q4', BLANK_SYMBOL): ('q5', BLANK_SYMBOL, LEFT),
    ('q5', 'a'): ('q5', 'a', LEFT),
    ('q5', 'b'): ('q5', 'b', LEFT),
    ('q5', 'c'): ('q5', 'c', LEFT),
    ('q5', 'x'): (Q_REJECT, 'x', RIGHT),
    ('q5', BLANK_SYMBOL): ('q6', BLANK_SYMBOL, LEFT),
    ('q6', 'a'): ('q7', 'A', RIGHT),
    ('q6', BLANK_SYMBOL): ('q7', 'A', RIGHT),
    ('q7', 'a'): ('q7', 'a', RIGHT),
    ('q7', 'b'): ('q8', 'B', RIGHT),
    ('q8', 'b'): ('q8', 'b', RIGHT),
    ('q8', 'c'): ('q9', 'C', LEFT),
    ('q8', 'C'): ('q8', 'C', RIGHT),
    ('q8', BLANK_SYMBOL): (Q_REJECT, BLANK_SYMBOL, RIGHT),
    ('q9', 'a'): ('q11', 'a', LEFT),
    ('q9', 'b'): ('q10', 'b', LEFT),
    ('q9', 'A'): ('q12', 'A', RIGHT),
    ('q9', 'B'): ('q9', 'b', LEFT),
    ('q9', 'C'): ('q9', 'C', LEFT),
    ('q10', 'b'): ('q10', 'b', LEFT),
    ('q10', 'B'): ('q7', 'B', RIGHT),
    ('q11', 'a'): ('q11', 'a', LEFT),
    ('q11', 'A'): ('q6', 'A', RIGHT),
    ('q12', 'b'): ('q12', 'b', RIGHT),
    ('q12', 'C'): ('q13', 'C', RIGHT),
    ('q13', 'c'): (Q_REJECT, 'c', RIGHT),
    ('q13', 'C'): ('q13', 'C', RIGHT),
    ('q13', BLANK_SYMBOL): (Q_ACCEPT, BLANK_SYMBOL, RIGHT)
}

tm3 = TuringMachine(states, input_alphabet, tape_alphabet, transition_function, start_state, accept_state, reject_state)