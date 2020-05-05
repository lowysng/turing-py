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
        self.current_state, write_symbol, move_head_direction = self.delta.get((self.current_state, self.read_tape()))
        self.write_tape(write_symbol)
        self.move_head(move_head_direction)
        return self.is_halt()

    def start_machine(self, verbose=True):
        if verbose:
            print('Starting Turing Machine...')
            self.print_configuration()
        halt = False
        while not halt:
            halt = self.compute_one_step()
            if verbose:
                self.print_configuration()
        if verbose:
            print('-------------------------------------------')
            print('Machine halted in the {0} configuration.'.format(self.halt_state))
            print('-------------------------------------------')
        return self.halt_state
    
    def read_tape(self):
        return self.tape[self.head]

    def write_tape(self, tape_symbol):
        self.tape[self.head] = tape_symbol
        return self.tape[self.head]

    def move_head(self, direction):
        if direction == LEFT:
            if self.head != 0:
                self.head = self.head - 1
        elif direction == RIGHT:
            if self.head == len(self.tape) - 1:
                self.tape.append(BLANK_SYMBOL)
            self.head = self.head + 1
        return self.tape[self.head]

    def is_halt(self):
        if self.current_state == Q_ACCEPT:
            self.halt_state = 'ACCEPT'
            return True
        elif self.current_state == Q_REJECT:
            self.halt_state = 'REJECT'
            return True
        else:
            return False
        
    def print_configuration(self):
        temp = self.tape[:]
        temp.insert(self.head, '[{0}]=>'.format(str(self.current_state)))
        temp = ''.join(temp)
        print('C: {0}'.format(temp))
        return temp
