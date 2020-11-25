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

class TM:
    ''' Object that correesponds to the turing machine '''

    def __init__(self):
        ''' Basic Constuctor '''
        self.sigma = []
        self.states = []
        self.current_state = None
        self.tape = None
        self.current_tape = None
        self.step = 0

    def create(self, sigma, states, tape):
        ''' Custom Constructor '''
        # Error checking occurs to ensure vars are properly instatiated
        start_bools = []
        ill_format = False
        if not (isinstance(sigma, list)
                or isinstance(states, list)
                or isinstance(tape, str)):
            ill_format = True
        if not ill_format:
            for a in range(0, states.__len__()):
                if isinstance(states[a], State):
                    start_bools.append(states[a].is_start())
                else:
                    ill_format = True
                    break
        if start_bools.count(True) != 1:
            ill_format = True
        # All States within self.states must have a unique uniq_id value.
        if not unique_states(states):
            ill_format = True
        if ill_format:
            print('Error: TM isntance unable to initialize due to ill formatted variables')
            sys.exit()
        self.sigma = sigma
        self.states = states
        for a in range(0, start_bools):
            if start_bools[a]:
                self.current_state = states[a] # self.current_state will be set to start state
        self.tape = tape
        self.current_tape = tape
        self.step = 0
