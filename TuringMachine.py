BLANK_SYMBOL = '[]'
Q_ACCEPT = 'q_accept'
Q_REJECT = 'q_reject'
LEFT = 'left'
RIGHT = 'right'

class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, transition_function, start_state, accept_state, reject_state):
        self.states = states
        self.sigma = input_alphabet
        self.gamma = tape_alphabet
        self.delta = transition_function
        self.start = start_state
        self.accept = accept_state
        self.reject = reject_state
    
    def load_input(self, input_string, verbose=True):
        if verbose:
            print('Loading input {0} ...'.format(input_string))
        for input_symbol in input_string:
            assert input_symbol in self.sigma, 'Input symbol {0} not found in input alphabet'.format(input_symbol)
        self.current_state = self.start
        self.tape = list(input_string)
        self.head = 0

    def compute_one_step(self):
        self.current_state, tape_symbol, LEFT_OR_RIGHT = self.delta.get((self.current_state, self.read_tape()))
        self.write_tape(tape_symbol)
        if LEFT_OR_RIGHT == LEFT:
            if self.head != 0:
                self.head = self.head - 1
        else:
            if self.head == len(self.tape) - 1:
                self.tape.append(BLANK_SYMBOL)
            self.head = self.head + 1
    
        if self.current_state == Q_ACCEPT:
            self.halt_state = 'ACCEPT'
            return True
        elif self.current_state == Q_REJECT:
            self.halt_state = 'REJECT'
            return True

        return False

    def start_machine(self, verbose=True):
        print('Starting Turing Machine...')
        if verbose:
            self.print_configuration()
        halt = False
        while not halt:
            halt = self.compute_one_step()
            if verbose:
                self.print_configuration()
        print('-------------------------------------------')
        print('Machine halted in the {0} configuration.'.format(self.halt_state))
        print('-------------------------------------------')
    
    def read_tape(self):
        return self.tape[self.head]

    def write_tape(self, tape_symbol):
        self.tape[self.head] = tape_symbol
        return self.tape[self.head]

    def print_configuration(self):
        temp = self.tape[:]
        temp.insert(self.head, '_{0}_'.format(str(self.current_state)))
        temp = ''.join(temp)
        print('C: {0}'.format(temp))
        return temp
