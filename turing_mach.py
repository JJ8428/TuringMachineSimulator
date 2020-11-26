''' Obj that the main script will use to Turing Machine '''
import sys
from state import State

def unique_states(states):
    ''' Accepts a list of states and makes all have unique uniq_id values '''
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
    if direction == 'L':
        return blank + tape
    # elif direction == 'R':
    return tape + blank

def find_state(states, uniq_id):
    ''' Find the State in states with a particular uniq_id '''
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
        # sigma[0] is the character that signifies blank (Provided TM text files use 'b' as blank)
        self.states = [] # List of all States in the TM
        self.current_state = None
        self.tape = None # Tape that TM shows each step will processing
        self.step = -1 # Count for number of steps
        self.head_index = 0 # Index of the head
        self.desc = None # Description of what TM should do (optional)

    def create(self, sigma, states, tape, desc=None):
        ''' Custom Constructor '''
        # Error checking occurs to ensure vars are proper types and correctly formatted
        start_bools = []
        ill_format = False
        if not (isinstance(sigma, list)
                or isinstance(states, list)
                or isinstance(tape, str)): # Check types
            ill_format = True
        if not ill_format:
            for a in range(0, states.__len__()):
                # Check types in list of transitions
                if isinstance(states[a], State):
                    start_bools.append(states[a].is_start())
                else:
                    ill_format = True
                    break
        # There can only be one start state in a TM
        if not ill_format and start_bools.count(True) != 1:
            ill_format = True
        # All States within self.states must have a unique uniq_id value.
        if not (ill_format and unique_states(states)):
            ill_format = True
        if ill_format:
            print('Error: TM isntance unable to initialize due to ill formatted variables')
            sys.exit()
        self.sigma = sigma
        self.states = states
        for a in range(0, start_bools):
            if start_bools[a]:
                self.current_state = states[a] # self.current_state is set to start state
                break
        self.tape = tape
        self.step = 0
        self.head_index = 0 # Head is placed on left most character
        self.desc = desc

    '''
    def partial_sane(self):
        # Return boolean if any states cannot be reached
        # Yes, I have to check final and start state, but I don't really care about those
        # This only serves as a warning for such states
        # Additionally, this method mainly used for debugging purposes
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
    '''

    def process(self):
        ''' TM will process the string '''
        ret = 'SIGMA: ' + str(self.sigma) + ' | BLANK CHAR: ' + self.sigma[0] + '\n'
        ret += 'INPUT: ' + self.tape + ' | TM DESC: ' + self.desc + '\n\n'
        ret += 'UNIQUE_ID, START STATE, FINAL/HALT STATE, TRANSITION(S):\n'
        for a in range(0, self.states.__len__()):
            ret += self.states[a].__str__() + '\n'
        ret += '\n'
        while True:
            self.step += 1
            ret += 'STEP:    ' + str(self.step) + ' | ' + 'STATE: ' + self.current_state.uniq_id()
            ret += 'POS:     '
            for a in range(0, self.head_index):
                ret += '  '
            ret += '*\nTAPE:    '
            for a in range(0, self.tape.__len__()):
                ret += self.tape[a] + ' '
            ret += '\n\n'
            list_tape = list(self.tape)
            if ['accept', 'reject'].__contains__(self.current_state.is_final):
                break # Halt, TM has reached a final state that either accepts/rejects
            to_read = list_tape[self.head_index]
            trans_info = self.current_state.read(to_read) # Format: [Write, Shift(L/R), State ID]
            list_tape = list(self.tape)
            list_tape[self.head_index] = trans_info[0] # Write new character State requires
            if trans_info[1] == 'L':
                self.head_index -= 1
            else: # shift == 'R':
                self.head_index += 1
            if self.head_index == -1:
                self.tape = buffer(self.tape, 'L', self.sigma[0])
            elif self.head_index == self.tape.__len__():
                self.tape = buffer(self.tape, 'R', self.sigma[0])
            # Update the variables in the TM
            self.tape = "".join(list_tape)
            self.current_state = find_state(self.states, trans_info[2])
        ret += 'FINAL STATE REACHED | STRING IS ' + self.current_state.is_final.upper() + '\n\n'
        return ret
