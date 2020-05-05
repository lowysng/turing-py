def get_states(n):
    return ['q' + str(x) for x in list(range(1, n + 1))]

def test_tm(tm, input_string, expected_result):
    tm.load_input(input_string, verbose=False)
    result = tm.start_machine(verbose=False)
    assert result == expected_result, 'Error on input {0}\nExpected: {1}\nGot: {2}'.format(input_string, expected_result, result)
    print('{0}: OK'.format(input_string))