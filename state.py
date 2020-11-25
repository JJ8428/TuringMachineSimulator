''' Turing Machine obj will utilize this represent each state '''
import sys

class State:
    ''' Simple object that correesponds to individual states in a turing machine '''

    def __init__(self):
        ''' Basic Constructor '''
        self.uniq_id = -1
        self.is_start = False
        self.is_final = False
        self.transitions = []

    def create(self, state_id, start, final, transitions):
        ''' Custom Constructor '''
        # Transitions will be a 2-D list with this format: [ [Read, Write, Shift(L/R), ID of new State] ]
        # Below error checking occurs to ensure list is properly instatiated
        ill_format = False
        if not (isinstance(state_id, int)
                or isinstance(transitions, list)
                or isinstance(start, bool)
                or isinstance(final, bool)):
            ill_format = True
        if not ill_format:
            for a in range(0, transitions.__len__()):
                if transitions[a].__len__() != 4 or isinstance(transitions[-1], int):
                    ill_format = True
                    break
        if ill_format:
            print('Error: State instance unable to initalize due to ill formatted variables')
            sys.exit()
        self.uniq_id = state_id
        self.is_start = start
        self.is_final = final
        self.transitions = transitions

    def on_reading(self, read):
        ''' Return information as what state does on reading 'read' '''
        index = -1
        for a in range(0, self.transitions.__len__()):
            if self.transitions[a][0] == read:
                index = a
                break
        if index == -1:
            print('Error: State instance did not have input encoded')
            sys.exit()
        return self.transitions[1:] # Return list in this format: [Write, Shift(L/R), State]
