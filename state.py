''' TM will utilize this obj represent each state '''
import sys

class State:
    ''' Simple object that correesponds to individual states in a turing machine '''

    def __init__(self):
        ''' Basic Constructor '''
        # Every State in a TM has a unique ID
        # States will indicate what State to tranition by giving uniq_id
        # self.uniq_id has type of str so TM's can be parsed from files of a specific syntax
        # Allows for easy naming convention
        self.uniq_id = 'Null'
        # Booleans if State is start state or final states
        self.is_start = False
        self.is_final_accept = False # Halt and Accept state
        self.is_final_reject = False # Halt and Reject state
        # transitions have to be a 2-D list with this format: [ [Read, Write, Shift(L/R), ID of new State] ]
        self.transitions = []

    def create(self, state_id, start, final_accept, final_reject, transitions):
        ''' Custom Constructor '''
        # Error checking occurs to ensure vars are proper types and correctly
        ill_format = False
        if not (isinstance(state_id, str)
                or isinstance(transitions, list)
                or isinstance(start, bool)
                or isinstance(final_accept, bool)
                or isinstance(final_reject, bool)): # Check types
            ill_format = True
        if not ill_format:
            for a in range(0, transitions.__len__()):
                # Check types in list of transitions
                if not(transitions[a].__len__() == 4 or isinstance(transitions[-1], int)):
                    ill_format = True
                    break
            if final_accept and final_reject: # Cannot both accept and reject as a final halt state
                ill_format = True
        # Error statement such that State characteristics are incorrect
        if ill_format:
            print('Error: State instance unable to initalize due to ill formatted variables')
            sys.exit()
        self.uniq_id = state_id
        self.is_start = start
        self.is_final_accept = final_accept
        self.is_final_reject = final_reject
        # Final states should not have any transitions
        # As soon as a final state is entered, the TM will halt
        if self.is_final_accept or self.is_final_reject:
            if transitions != []:
                print('Warning: Transitions on final halt accept/reject states are detected but will be ignored')
            self.transitions = []
        else:
            self.transitions = transitions

    def read(self, to_read):
        ''' Return information as what state does on reading input 'read' '''
        index = -1
        for a in range(0, self.transitions.__len__()):
            if self.transitions[a][0] == to_read:
                index = a
                break
        # Error statement such that current State has no transition for input 'read'
        if index == -1:
            print('Error: State instance did not have transition encoded')
            sys.exit()
        return self.transitions[index][1:] # Return list in this format: [Write(Sigma), Shift(L/R), State(uniq_id)]

    def __str__(self):
        ''' String of State to print '''
        toRet = self.uniq_id + ', ' + self.is_start + ', ' + self.is_final_accept + ', ' + self.is_final_reject
        for a in range(0, self.transitions):
            toRet += ', (' + self.transitions[a][0] + '|' + self.transitions[a][1] + '|' + self.transitions[a][2] + '|' + self.transitions[a][3] + ')'
        toRet += '\n'
        return toRet