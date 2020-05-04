from FA import NFA
from util import get_states, generate_random_string

EPSILON = 'epsilon'
BINARY_ALPHABET = ['0', '1']
TEST_STRINGS = []
TEST_ITERATION = 10

"""This NFA accepts strings that either
(1) begin with a 0 and ends with a 1, or
(2) have at least 3 1's
"""
transition_dict = {
    ('q1', '0'): (),
    ('q1', '1'): (),
    ('q1', EPSILON): ('q2', 'q5'),
    ('q2', '0'): ('q3'),
    ('q2', '1'): (),
    ('q2', EPSILON): (),
    ('q3', '0'): ('q3'),
    ('q3', '1'): ('q3', 'q4'),
    ('q3', EPSILON): (),
    ('q4', '0'): (),
    ('q4', '1'): (),
    ('q4', EPSILON): (),
    ('q5', '0'): ('q5'),
    ('q5', '1'): ('q6'),
    ('q5', EPSILON): (),
    ('q6', '0'): ('q6'),
    ('q6', '1'): ('q7'),
    ('q6', EPSILON): (),
    ('q7', '0'): ('q7'),
    ('q7', '1'): ('q8'),
    ('q7', EPSILON): (),
    ('q8', '0'): ('q8'),
    ('q8', '1'): ('q8'),
    ('q8', EPSILON): (),
}

nfa = NFA(get_states(8), BINARY_ALPHABET, transition_dict, 'q1', ['q4', 'q8'])
print("nfa accepts strings that either: begins with 0 and ends with 1, or has at least 3 1's")

for _ in range(TEST_ITERATION):
    TEST_STRINGS.append(generate_random_string(BINARY_ALPHABET))

for string in TEST_STRINGS:
    begins_with_0 = string[0] == '0'
    ends_with_1 = string[len(string) - 1] == '1'
    count_one = 0
    for s in string:
        if s == '1':
            count_one += 1
    at_least_3_one = count_one > 2
    
    condition_1 = begins_with_0 and ends_with_1
    condition_2 = at_least_3_one

    if nfa.accept(string, verbose=False) != (condition_1 or condition_2):
        print('assertion failed: {0}, should be {1}'.format(string, condition_1 or condition_2))
    else:
        print('assertion passed: {0} => {1}'.format(string, nfa.accept(string)))