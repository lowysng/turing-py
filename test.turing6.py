from turing6 import tm6
from util import test_tm

test_strings = [
    '0', '1', '00', '01', '10', '11',
    '000', '001', '010', '011', '100', '101', '110', '111',
    '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
    '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
]

for string in test_strings:
    zero_count = 0
    one_count = 0
    for s in string:
        if s == '0':
            zero_count += 1
        elif s == '1':
            one_count += 1

    if zero_count * one_count == 0:
        expected_result = 'ACCEPT'
    elif zero_count == one_count * 2:
        expected_result = 'REJECT'
    else:
        expected_result = 'ACCEPT'

    test_tm(tm6, string, expected_result)