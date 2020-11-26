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

# TODO: What if you need to refer to blanks preappended to the string and not enough blanks exist?


def buffer(tape, direction):
    ''' Adds blanks in the tape if necessary '''
    # tape is the string we are to prepend/append a blank to
    # direction (L/R) will tell if the tape needs to be preappened/appened to
    return 1

def find_state(states, uniq_id):
    ''' Find the State in states with a particular uniq_id '''
    for a in range(0, states.__len__()):
        if states[a].uniq_id == uniq_id:
            return states[a]

class TM:
    ''' Object that correesponds to the turing machine '''

    def __init__(self):
        ''' Basic Constuctor '''
        self.sigma = [] # Sigma is list of characters that are used as the TM's alphabet
        # sigma[0] is the character that signifies blank (Provided TM text files use 'b' as blank)
        self.states = [] # List of all States in the TM
        self.current_state = None
        self.tape = None # Original tape (helps when debugging)
        self.current_tape = None # Tape that TM shows each step will processing
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
                self.current_state = states[a] # self.current_state set start state
        self.tape = tape
        self.current_tape = tape
        self.step = 0
        self.head_index = 0 # Head is placed on left most character
        self.desc = desc

    def check_strays(self):
        ''' Return boolean if any stray states (states that cannot be transitioned into) '''
        reachable = []
        for a in range(0, self.states.__len__()):
            reachable.append(self.states[a].uniq_id)
        for a in range(0, self.states.__len__()):
            for b in range(0, self.states[a].transitions.__len__()):
                if (reachable.__contains__(self.states[a].transitions[b][-1])
                    and self.states[a].is_start == False):
                    reachable.remove(self.states[a].transitions[b][-1])
        return reachable.__len__() == 0

    def process(self):
        ''' TM will process the string '''
        toPrint = 'Sigma: ' + str(self.sigma) + ' | Blank Char: ' + self.sigma[0] + '\n'
        toPrint += 'Input: ' + self.tape + ' | TM Desc: ' + self.desc + '\n\n'
        toPrint += 'Unique_ID, Start State, Halt Accept State, Halt Reject State, Transitions:\n'
        for a in range(0, self.states.__len__()):
            toPrint += self.states[a].__str__() + '\n'
        toPrint += '\n'
        while True:
            if self.current_state.is_final_accept or self.current_state.is_final_reject:
                break # Halt, since the TM has reached a final state that either accepts/rejects
            toPrint += ''
            list_tape = list(self.current_tape)
            to_read = list_tape[self.head_index]
            transition_info = self.current_state.read(to_read) # List in this format: [Write(Sigma), Shift(L/R), State(uniq_id)]
            list_tape[self.head_index] = transition_info[0] # Write the new character the state needs us to write
            if transition_info[1] == 'L':
                self.head_index -= 1
            else: # shift == 'R':
                self.head_index += 1
            # TODO buffer()
            self.current_tape = "".join(list_tape)
            self.current_state = find_state(self.states, transition_info[2])
            self.step += 1
            toPrint += ''
        if self.current_state.is_final_accept:
            toPrint += 'accepted woo hoo'
        else: # self.current_state.is_final_reject: 
            toPrint += 'rejected boo hoo'
        
        

