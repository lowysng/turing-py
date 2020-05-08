BLANK_SYMBOL = '[]'
Q_ACCEPT = 'q_accept'
Q_REJECT = 'q_reject'
LEFT = 'left'
RIGHT = 'right'

from TuringMachine import TuringMachine
from util import get_states
from dfa1 import dfa1

description = 'This Turing Machine decides the language A = { w | w is a string accepted by dfa1 }'
states = get_states(17) + [Q_ACCEPT, Q_REJECT]
input_alphabet = ['0', '1', '#'] + dfa1.states
tape_alphabet = ['0', '1', 'x', '#', '@', BLANK_SYMBOL] + dfa1.states
start_state = 'q1'
accept_state = Q_ACCEPT
reject_state = Q_REJECT
transition_function = {
    ('q1', '0'): ('q1', '0', RIGHT),
    ('q1', '1'): ('q1', '1', RIGHT),
    ('q1', BLANK_SYMBOL): ('q2', '#', RIGHT),
    ('q2', BLANK_SYMBOL): ('q3', dfa1.start_state, LEFT),
    ('q3', '#'): ('q4', '#', LEFT),
    ('q4', '0'): ('q5', '@', LEFT),
    ('q4', '1'): ('q7', '@', LEFT),
    ('q5', '0'): ('q6', '0', RIGHT),
    ('q5', '1'): ('q6', '1', RIGHT),
    ('q5', '@'): ('q9', '0', LEFT),
    ('q6', '@'): ('q4', '0', LEFT),
    ('q7', '0'): ('q8', '0', RIGHT),
    ('q7', '1'): ('q8', '1', RIGHT),
    ('q7', '@'): ('q9', '1', LEFT),
    ('q8', '@'): ('q4', '1', LEFT),
    ('q9', '0'): ('q10', 'x', RIGHT),
    ('q9', '1'): ('q12', 'x', RIGHT),
    ('q10', '0'): ('q10', '0', RIGHT),
    ('q10', '1'): ('q10', '1', RIGHT),
    ('q10', '#'): ('q11', '#', RIGHT),
    ('q11', 'Q1'): ('q14', 'Q2', LEFT),
    ('q11', 'Q2'): ('q14', 'Q2', LEFT),
    ('q11', 'Q3'): ('q14', 'Q2', LEFT),
    ('q11', 'Q4'): ('q14', 'Q4', LEFT),
    ('q12', '0'): ('q12', '0', RIGHT),
    ('q12', '1'): ('q12', '1', RIGHT),
    ('q12', '#'): ('q13', '#', RIGHT),
    ('q13', 'Q1'): ('q14', 'Q4', LEFT),
    ('q13', 'Q2'): ('q14', 'Q3', LEFT),
    ('q13', 'Q3'): ('q14', 'Q3', LEFT),
    ('q13', 'Q4'): ('q14', 'Q4', LEFT),
    ('q14', '#'): ('q15', '#', LEFT),
    ('q15', '0'): ('q16', '0', LEFT),
    ('q15', '1'): ('q16', '1', LEFT),
    ('q15', 'x'): ('q17', 'x', RIGHT),
    ('q16', '0'): ('q16', '0', LEFT),
    ('q16', '1'): ('q16', '1', LEFT),
    ('q16', 'x'): ('q9', 'x', RIGHT),
    ('q17', '#'): ('q17', '#', RIGHT),
    ('q17', 'Q1'): (Q_REJECT, 'Q1', RIGHT),
    ('q17', 'Q2'): (Q_REJECT, 'Q2', RIGHT),
    ('q17', 'Q3'): (Q_ACCEPT, 'Q3', RIGHT),
    ('q17', 'Q4'): (Q_REJECT, 'Q4', RIGHT),
}

tm7 = TuringMachine(
    states,
    input_alphabet,
    tape_alphabet,
    transition_function,
    start_state,
    accept_state,
    reject_state,
    description
)