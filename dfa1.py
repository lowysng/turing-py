from FA import DFA

states = ['Q1', 'Q2', 'Q3', 'Q4']
alphabet = ['0', '1']
transition_dict = {
    ('Q1', '0'): 'Q2',
    ('Q1', '1'): 'Q4',
    ('Q2', '0'): 'Q2',
    ('Q2', '1'): 'Q3',
    ('Q3', '0'): 'Q2',
    ('Q3', '1'): 'Q3',
    ('Q4', '0'): 'Q4',
    ('Q4', '1'): 'Q4'
}
start_state = 'Q1'
accept_states = ['Q3']

dfa1 = DFA(states, alphabet, transition_dict, start_state, accept_states)