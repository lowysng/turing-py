from DFA import DFA, test_dfa
from util import get_states, generate_random_string

AB_ALPHABET = ['a', 'b']
AB_TEST_STRINGS = []
for _ in range(20):
    AB_TEST_STRINGS.append(generate_random_string(AB_ALPHABET))

transition_dict = {
    ('q1', 'a'): 'q3',
    ('q1', 'b'): 'q4',
    ('q2', 'a'): 'q4',
    ('q2', 'b'): 'q3',
    ('q3', 'a'): 'q1',
    ('q3', 'b'): 'q2',
    ('q4', 'a'): 'q2',
    ('q4', 'b'): 'q1',
}
dfa = DFA(get_states(3), AB_ALPHABET, transition_dict, 'q1', ['q2'])
print("dfa accepts strings with even length and odd number of a's")
for string in AB_TEST_STRINGS:
    count_a = 0
    for s in string:
        if s == 'a':
            count_a += 1
    count_a_is_odd = count_a % 2 == 1
    is_even = len(string) % 2 == 0
    if dfa.accept(string) != is_even and count_a_is_odd:
        print('assertion failed: {0}, should be {1}'.format(string, is_even and count_a_is_odd))
    else:
        print('{0} => {1}'.format(string, dfa.accept(string)))