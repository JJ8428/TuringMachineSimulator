''' Obj that the main script will use to Turing Machine '''
import sys
from state import State

def unique_states(states):
    ''' Accepts a list of states and makes all have unique uniq_id values '''
    # pylint: disable=invalid-name
    good_format = True
    for a in range(0, states.__len__()):
        for b in range(a + 1, states.__len__()):
            if states[a].uniq_id == states[b].uniq_id:
                good_format = False
                break
            if not good_format:
                break
    return good_format

def buffer(tape, direction, blank):
    ''' Adds blanks in the tape if necessary '''
    # Assume tape has infinite blanks both before hand and after hand
    if direction == 'L':
        return blank + tape
    # elif direction == 'R':
    return tape + blank

def find_state(states, uniq_id):
    ''' Find the State in states with a particular uniq_id '''
    # pylint: disable=invalid-name
    ret = None
    for a in range(0, states.__len__()):
        if states[a].uniq_id == uniq_id:
            ret = states[a]
            break
    return ret

class TM:
    ''' Object that correesponds to the turing machine '''

    def __init__(self):
        ''' Basic Constuctor '''
        self.sigma = [] # Sigma is list of characters that are used as the TM's alphabet
        self.states = [] # List of all States in the TM
        self.current_state = None # The current State the TM is on
        self.tape = None # Tape that TM shows each step will processing
        self.step = -1 # Count for number of steps
        self.head_index = 0 # Index of the head
        self.desc = None # Description of what TM does

    def create(self, sigma, states, desc=None):
        ''' Custom Constructor '''
        # pylint: disable=invalid-name
        # Error checking occurs to ensure vars are proper types and correctly formatted
        start_bools = []
        ill_format = False
        error = ''
        if not (isinstance(sigma, list)
                or isinstance(states, list)): # Check types
            ill_format = True
            error += 'self (TM) .create() has input of wrong types.\n'
        if not ill_format:
            for a in range(0, states.__len__()):
                # Check types in list of transitions
                if isinstance(states[a], State):
                    start_bools.append(states[a].is_start)
                else:
                    ill_format = True
                    # This error only occurs for a poorly designed __main__
                    error += 'States did not load correctly. This is due to poor handling in __main__.\n'
                    break
        # There can only be one start state in a TM
        if not ill_format and start_bools.count(True) != 1:
            ill_format = True
            error += 'TM instance can only have one start state.'
        # All States within self.states must have a unique uniq_id value.
        if not (ill_format or unique_states(states)):
            ill_format = True
            error = 'TM instance must have states with each having unique uniq_id.\n'
        if ill_format:
            print('Error: TM instance unable to initialize due to ill formatted variables')
            print('\n' + error)
            sys.exit()
        self.sigma = sigma
        self.states = states
        for a in range(0, start_bools.__len__()):
            if start_bools[a]:
                self.current_state = states[a] # self.current_state is set to start state
                break
        self.step = -1
        self.head_index = 0 # Head is placed on left most character
        self.desc = desc

    def partial_sane(self):
        '''
        Yes, I have to check final and start state, but I don't really care about those
        This only serves as a warning for states that cannot be reached from other states
        '''
        # pylint: disable=invalid-name
        reachable = []
        for a in range(0, self.states.__len__()):
            if not self.states[a].is_start:
                reachable.append(self.states[a].uniq_id)
        for a in range(0, self.states.__len__()):
            for b in range(0, self.states[a].transitions.__len__()):
                if (reachable.__contains__(self.states[a].transitions[b][-1])
                        and not self.states[a].is_start):
                    reachable.remove(self.states[a].transitions[b][-1])
        return reachable.__len__() == 0

    def process(self):
        ''' TM will process the string '''
        # pylint: disable=invalid-name
        if self.tape == None:
            print('Error: Tape is not loaded in TM instance.')
            print('\n' + 'It is very likely the input is not encoded correctly')
            sys.exit()
        # Set text to have parameters shown
        ret = 'SIGMA: '
        for a in range(0, self.sigma.__len__()):
            ret += self.sigma[a] + ' '
        ret += '| BLANK CHAR: ' + self.sigma[0] + '\n'
        ret += 'INPUT: ' + self.tape + ' | TM DESC: ' + self.desc + '\n'
        ret += 'UNIQUE_ID, START STATE, FINAL/HALT STATE, TRANSITION(S):\n'
        for a in range(0, self.states.__len__()):
            ret += self.states[a].__str__()
        ret += '\n'
        while True:
            self.step += 1
            list_tape = list(self.tape)
            # Have text built to show process
            ret += 'STEP:    ' + str(self.step) + ' | ' + 'STATE: '  + self.current_state.uniq_id
            ret += '\nPOS:     '
            for a in range(0, self.head_index):
                ret += '  '
            ret += '*\nTAPE:    '
            for a in range(0, self.tape.__len__()):
                ret += self.tape[a] + ' '
            ret += '\n\n'
            if ['accept', 'reject'].__contains__(self.current_state.is_final):
                break # Halt, TM has reached a final state that either accepts/rejects
            to_read = list_tape[self.head_index]
            trans_info = self.current_state.read(to_read) # Format: [Write, Shift(L/R), State ID]
            list_tape[self.head_index] = trans_info[0] # Write new character state requires
            # Update the head_index
            if trans_info[1] == 'L':
                self.head_index -= 1
            elif trans_info[1] == 'R': # shift == 'R':
                self.head_index += 1
            # Update the variables in the TM
            self.tape = "".join(list_tape)
            # Buffer the tape is necessary (adding blanks)
            # Assumes tape is infinite length with blanks before and after string
            if self.head_index == -1:
                self.tape = buffer(self.tape, 'L', self.sigma[0])
                self.head_index = 0
            elif self.head_index == self.tape.__len__():
                self.tape = buffer(self.tape, 'R', self.sigma[0])
            self.current_state = find_state(self.states, trans_info[2])
        ret += 'FINAL/HALT STATE REACHED | STRING IS ' + self.current_state.is_final.upper() + 'ED\n'
        return ret

    def load_tape(self, tape):
        ''' Reset the TM and load tape '''
        # Allows for TM to be used repeatedly
        self.tape = tape
        self.step = -1
        self.head_index = 0
