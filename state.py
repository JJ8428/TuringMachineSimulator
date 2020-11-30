''' TM will utilize this obj represent each state '''
import sys

class State:
    ''' Simple object that correesponds to individual states in a TM '''

    def __init__(self):
        ''' Basic Constructor '''
        # State unique str id
        # If the uniq_id has str of final in it any way, it accepts when reached
        self.uniq_id = None
        # Booleans if State is a start state or halt state
        self.is_start = None
        self.is_halt = None
        # transitions are 2-D list with format: [ [Read, Write, Shift(L/R), State ID] ]
        self.transitions = []

    def create(self, state_id, start, halt, transitions=None):
        ''' Custom Constructor '''
        # pylint: disable=invalid-name
        # Error checking occurs to ensure vars are proper types and correctly
        ill_format = False
        error = ''
        # Check type of variables
        if not (isinstance(state_id, str)
                or (isinstance(transitions, list) or transitions is None)
                or isinstance(start, bool)
                or isinstance(halt, bool)):
            ill_format = True
            error += 'self (State) .create() has input of wrong type(s).\n'
        if not ill_format and transitions is not None:
            for a in range(0, transitions.__len__()):
                # Check types in list of transitions
                if transitions[a].__len__() != 4:
                    ill_format = True
                    error += 'Transitions are not recognized'
                    error += '\nPoint of error: ' + transitions
                    break
        # Error statement if issues arise above
        if ill_format:
            print('State Error: State instance unable to initalize due to ill formatted variables')
            print('\n' + error)
            sys.exit()
        self.uniq_id = state_id
        self.is_start = start
        self.is_halt = halt
        self.transitions = transitions

    def read(self, to_read):
        ''' Return information as what State does on reading input 'to_read' '''
        # pylint: disable=invalid-name
        index = -1
        if self.transitions is not None:
            for a in range(0, self.transitions.__len__()):
                if self.transitions[a][0] == to_read:
                    index = a
                    break
        # Error statement such that current State has no transition for input 'read'
        if index == -1:
            return None # TM will halt and reject
        return self.transitions[index][1:] # Return list in this format: [Write, Shift(L/R), State]

    def __str__(self):
        ''' String of State to print '''
        # pylint: disable=invalid-name
        ret = (self.uniq_id + ', ' +
               str(self.is_start) + ', ' +
               str(self.is_halt))
        if self.transitions is not None:
            for a in range(0, self.transitions.__len__()):
                ret += (', ' + self.transitions[a][0] +
                        '|' + self.transitions[a][1] +
                        '|' + self.transitions[a][2] +
                        '|' + self.transitions[a][3])
        ret += '\n'
        return ret
