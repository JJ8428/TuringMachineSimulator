''' Builds the TM obj from the file '''
# Remember, we have to load the tape(s) manually

import re
from state import State
from turing_mach import TM

def assemble(buildpath):
    ''' Constructs the TM with State obj TM instance '''
    # pylint: disable=invalid-name
    # pylint: disable=pointless-string-statement
    read = open(buildpath, 'r')
    build = ''
    for line in read.readlines():
        build += re.sub(' +', ' ', line).replace('\n ', '\n').replace(' \n', '\n')
    read.close()
    while build[-1] == '\n':
        build = build[:-1]
    build = build.split('\n\n')
    for a in range(0, build.__len__()):
        build[a] = build[a].split('\n')
        for b in range(0, build[a].__len__()):
            if build[a][b] == ['']:
                build[a].remove([''])
            else:
                build[a][b] = build[a][b].split(' ')
    # Get sigma and state_ids
    sigma = ['b']
    state_ids = []
    for a in range(0, build.__len__()):
        for b in range(0, build[a].__len__()):
            if not sigma.__contains__(build[a][b][1]):
                sigma.append(build[a][b][1])
            if not sigma.__contains__(build[a][b][3]):
                sigma.append(build[a][b][3])
            if not state_ids.__contains__(build[a][b][0]):
                state_ids.append(build[a][b][0])
            if not state_ids.__contains__(build[a][b][2]):
                state_ids.append(build[a][b][2])
    '''
        Assumptions:
        START state is the state that has START in its name/id
        HALT states are detected if no transitions are found for that state
        - Will accept if HALT state has FINAL in its name/id
        - Will reject if HALT state does not have FINAL in its name
    '''
    states = []
    for a in range(0, build.__len__()):
        state = State()
        transitions = []
        uniq_id = build[a][0][0]
        # Assume the start state has a uniq_id with str of start in it
        if uniq_id.upper().__contains__('START'):
            start = 1
        else:
            start = 0
        for b in range(0, build[a].__len__()):
            transitions.append([build[a][b][1],
                                build[a][b][3],
                                str(build[a][b][4])[0],
                                build[a][b][2]])
        state.create(uniq_id, start, 0, transitions)
        states.append(state)
    built = [] # States we have built (not halt states)
    for state in states:
        built.append(state.uniq_id)
    remaining = [] # States to build (halt states)
    for a in range(0, state_ids.__len__()):
        if not built.__contains__(state_ids[a]):
            remaining.append(state_ids[a])
    # Create the final states
    for halt_state in remaining:
        state = State()
        state.create(halt_state, 0, 1)
        states.append(state)
    to_ret = TM()
    to_ret.create(sigma, states, buildpath)
    return to_ret
