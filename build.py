''' Builds the TM obj from the file '''
# Remember, we have to load the tape(s) manually

import sys
from state import State
from turing_mach import TM

def build(buildpath):
    ''' Constructs the TM with State obj TM instance '''
    read = open(buildpath, 'r')
    # Extract the sigma parameter
    # Format: sigma = [..., ..., ...]
    sigma = read.readline().strip()
    sigma = sigma.replace(' ', '')
    sigma = sigma.replace('sigma', '')
    sigma = sigma.replace('=', '')
    sigma = sigma.replace('[', '')
    sigma = sigma.replace(']', '')
    sigma = sigma.split(',')
    # Format: desc = ...
    desc = read.readline().replace('desc', '').replace('=', '').replace('\n', '')
    # Format: state_ids = [..., ..., ...]
    state_ids = read.readline().strip()
    state_ids = state_ids.replace(' ', '')
    state_ids = state_ids.replace('state_ids', '')
    state_ids = state_ids.replace('=', '')
    state_ids = state_ids.replace('[', '')
    state_ids = state_ids.replace(']', '')
    state_ids = state_ids.split(',')
    read.close()
    read = open(buildpath, 'r')
    states = []
    line_count = 0
    for line in read.readlines():
        if line_count < 3: # Previous 2 lines already read for sigma and desc parameters
            line_count += 1
            continue
        line = line.strip()
        line = line.replace(' ', '')
        line = line.split(',')
        state_id = line[0]
        try:
            start = bool(int(line[1]))
        except ValueError:
            print('Build Error: Transitions in build path are ill format')
            sys.exit()
        final = line[2]
        transitions = []
        for a in range(3, line.__len__()):
            tmp = line[a].split('|')
            if (not (sigma.__contains__(tmp[0]) and sigma.__contains__(tmp[1]))
                    or not ['L', 'R'].__contains__(tmp[2])
                    or not state_ids.__contains__(tmp[3])):
                print('Build Error: Transitions in build path are ill format')
                sys.exit()
            transitions.append(tmp)
        # Build the states
        state = State()
        state.create(state_id, start, final, transitions)
        states.append(state)
    read.close()
    # tape will be loaded in the main script
    to_ret = TM()
    to_ret.create(sigma, states, 'yet to load', desc)
    return to_ret

tm = build('test1.txt')
tm.tape = '00'
print(tm.process())