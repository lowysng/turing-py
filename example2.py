from FA import NFA
from util import get_states, generate_random_string
from random import randint

EPSILON = 'epsilon'
BINARY_ALPHABET = ['0', '1']
TEST_STRINGS = []
TEST_CORRECT_OUTPUTS = []
TEST_ITERATION = 10

"""This NFA accepts strings that are concatenations of w1 and w2, where
(1) w1 is a string that has length at most 5, and
(2) w2 is a string that has a 1 at every odd position
"""
transition_dict = {
    ('q1', '0'): ('q2'),
    ('q1', '1'): ('q2'),
    ('q1', EPSILON): ('q8'),
    ('q2', '0'): ('q3'),
    ('q2', '1'): ('q3'),
    ('q2', EPSILON): ('q8'),
    ('q3', '0'): ('q4'),
    ('q3', '1'): ('q4'),
    ('q3', EPSILON): ('q8'),
    ('q4', '0'): ('q5'),
    ('q4', '1'): ('q5'),
    ('q4', EPSILON): ('q8'),
    ('q5', '0'): ('q6'),
    ('q5', '1'): ('q6'),
    ('q5', EPSILON): ('q8'),
    ('q6', '0'): ('q7'),
    ('q6', '1'): ('q7'),
    ('q6', EPSILON): ('q8'),
    ('q7', '0'): ('q7'),
    ('q7', '1'): ('q7'),
    ('q7', EPSILON): (),
    ('q8', '0'): ('q11'),
    ('q8', '1'): ('q9'),
    ('q8', EPSILON): (),
    ('q9', '0'): ('q10'),
    ('q9', '1'): ('q10'),
    ('q9', EPSILON): (),
    ('q10', '0'): ('q11'),
    ('q10', '1'): ('q9'),
    ('q10', EPSILON): (),
    ('q11', '0'): ('q1'),
    ('q11', '1'): ('q1'),
    ('q11', EPSILON): (),
}

nfa = NFA(get_states(11), BINARY_ALPHABET, transition_dict, 'q1', ['q8', 'q9', 'q10'])

for _ in range(TEST_ITERATION):
    string = generate_random_string(BINARY_ALPHABET)

    if len(string) < 6:
        TEST_STRINGS.append(string)
        TEST_CORRECT_OUTPUTS.append(True)
    else:
        i = 0
        while i < 5:
            one_at_odd = True
            string_one_at_odd = string[i:]
            for idx, s in enumerate(string_one_at_odd):
                if (idx + 1) % 2 == 1:
                    if s != '1':
                        one_at_odd = False
            if one_at_odd:
                TEST_STRINGS.append(string)
                TEST_CORRECT_OUTPUTS.append(one_at_odd)
                break
            else:
                i += 1
        if not one_at_odd:
            TEST_STRINGS.append(string)
            TEST_CORRECT_OUTPUTS.append(one_at_odd)


for idx, string in enumerate(TEST_STRINGS):

    if nfa.accept(string, verbose=False) != TEST_CORRECT_OUTPUTS[idx]:
        print('assertion failed: {0}, should be {1}'.format(string, TEST_CORRECT_OUTPUTS[idx]))
    else:
        print('assertion passed: {0} => {1}'.format(string, nfa.accept(string)))