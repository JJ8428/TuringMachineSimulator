''' Builds the TM obj from the file '''
# Remember, we have to load the tape(s) manually

import sys
# import re
from state import State
from turing_mach import TM

# This is a method that reads from a different format of input files
def assemble2(buildpath):
    # Constructs the TM with State obj TM instance
    # pylint: disable=invalid-name
    read = open(buildpath, 'r')
    # Format: sigma = [..., ..., ...]
    sigma = read.readline().strip()
    sigma = sigma.replace(' ', '')
    sigma = sigma.replace('sigma', '')
    sigma = sigma.replace('=', '')
    sigma = sigma.replace('[', '')
    sigma = sigma.replace(']', '')
    sigma = sigma.split(',')
    # Format: desc = ...
    desc = read.readline().replace('desc', '')
    desc = desc.replace('=', '')
    desc = desc.replace('\n', '')
    # Format: state_ids = [..., ..., ...]
    state_ids = read.readline().strip()
    state_ids = state_ids.replace(' ', '')
    state_ids = state_ids.replace('state_ids', '')
    state_ids = state_ids.replace('=', '')
    state_ids = state_ids.replace('[', '')
    state_ids = state_ids.replace(']', '')
    state_ids = state_ids.split(',')
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
        if not [0, 1].__contains__(int(line[1])):
            print('Assemble Error: Build path should have start states only determined as 0 or 1.')
            sys.exit()
        try:
            start = bool(int(line[1]))
        except ValueError:
            print('Build Error: Transitions in build path are ill format')
            sys.exit()
        final = line[2]
        transitions = []
        for a in range(3, line.__len__()):
            tmp = line[a].split('|')
            # Checks if transitions are encoded correctly
            if (tmp.__len__() != 4):
                print('Build Error: Transitions in build path are ill format')
                print('\nParsing occured on the following line: ' + line[a])
                sys.exit()
            if (not sigma.__contains__(tmp[0])
                    or not sigma.__contains__(tmp[1])
                    or not ['L', 'R'].__contains__(tmp[2])
                    or not state_ids.__contains__(tmp[3])):
                print('Build Error: Transitions in build path are ill format')
                print('\nParsing occured on the following line: ' + line[a])
                sys.exit()
            transitions.append(tmp)
        # Build the states
        state = State()
        state.create(state_id, start, final, transitions)
        states.append(state)
    read.close()
    # tape will be loaded in the main script
    to_ret = TM()
    to_ret.create(sigma, states, desc)
    return to_ret