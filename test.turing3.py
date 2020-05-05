from turing3 import tm3
from util import test_tm

test_strings = [
    'abc',
    'ab',
    'aabc',
    'aabbcccc',
    'aabcc',
    'abbcc',
    'aaaabbbbcccccccccccccccc'
]

for string in test_strings:
    a_count = 0
    b_count = 0
    c_count = 0
    for s in string:
        if s == 'a':
            a_count += 1
        elif s == 'b':
            b_count += 1
        elif s == 'c':
            c_count += 1
                
    product = a_count * b_count

    if product == 0 or c_count == 0:
        expected_result = 'REJECT'
    elif product == c_count:
        expected_result = 'ACCEPT'
    else:
        expected_result = 'REJECT'

    test_tm(tm3, string, expected_result)