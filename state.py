''' TM will utilize this obj represent each state '''
import sys

class State:
    ''' Simple object that correesponds to individual states in a TM '''

    def __init__(self):
        ''' Basic Constructor '''
        # Every State in a TM has a unique ID
        # States will indicate what State to tranition by giving uniq_id of the State to transfer to
        # self.uniq_id has type of str so TM's can be parsed from files of a specific syntax
        # Allows for easy naming convention
        self.uniq_id = None
        # Booleans if State is a start state or final State
        self.is_start = False
        # String if 'accept', 'reject' final State or 'none' if not Final State
        self.is_final = None
        # transitions are 2-D list with format: [ [Read, Write, Shift(L/R), State ID] ]
        self.transitions = []

    def create(self, state_id, start, final, transitions):
        ''' Custom Constructor '''
        # Error checking occurs to ensure vars are proper types and correctly
        ill_format = False
        if not (isinstance(state_id, str)
                or isinstance(transitions, list)
                or isinstance(start, bool)
                or isinstance(final, str)):
            ill_format = True
        if not ill_format:
            for a in range(0, transitions.__len__()):
                # Check types in list of transitions
                if not(transitions[a].__len__() == 4 or isinstance(transitions[-1], int)):
                    ill_format = True
                    print('bb')
                    break
            if not ['not', 'accept', 'reject'].__contains__(final):
                ill_format = True
        # Error statement such that State characteristics are incorrect
        if ill_format:
            print('State Error: State instance unable to initalize due to ill formatted variables')
            sys.exit()
        self.uniq_id = state_id
        self.is_start = start
        self.is_final = final
        # Final states should not have any transitions
        # As soon as a final state is entered, the TM will halt
        if ['accept', 'reject'].__contains__(self.is_final):
            if transitions != []:
                print('State Warning: Transitions on final/halt states are detected but will be ignored')
            self.transitions = []
        else:
            self.transitions = transitions

    def read(self, to_read):
        ''' Return information as what State does on reading input 'to_read' '''
        index = -1
        for a in range(0, self.transitions.__len__()):
            if self.transitions[a][0] == to_read:
                index = a
                break
        # Error statement such that current State has no transition for input 'read'
        if index == -1:
            print('Error: State instance did not have transition encoded for input')
            sys.exit()
        return self.transitions[index][1:] # Return list in this format: [Write, Shift(L/R), State]

    def __str__(self):
        ''' String of State to print '''
        ret = (self.uniq_id + ', ' +
               str(self.is_start) + ', ' +
               self.is_final.upper())
        for a in range(0, self.transitions.__len__()):
            ret += (', (' + self.transitions[a][0] +
                    '|' + self.transitions[a][1] +
                    '|' + self.transitions[a][2] +
                    '|' + self.transitions[a][3] + ')')
        ret += '\n'
        return ret
