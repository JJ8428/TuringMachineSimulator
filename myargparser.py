''' Simple argparser '''
import argparse
import sys

def parser():
    ''' Simple parser to check build, input, and output path '''
    # 3 arguments: build, input, output
    # build is a file with the states defined
    # input is a file where the string(s) are taking as input
    # output is a file where the processed string(s) are saved
    to_parse = argparse.ArgumentParser(description='Simulate the behavior of a Turing Machine')
    to_parse.add_argument('-b', '--build', type=str, metavar='', required=True,
                          help='Path of file containing Turing Machine transitions')
    to_parse.add_argument('-i', '--input', type=str, metavar='', required=True,
                          help='String for Turing Machine to process')
    args = to_parse.parse_args()
    # Check if paths are valid files
    error = False
    try:
        r_tmp = open(args.build, 'r')
        r_tmp.close()
    except FileNotFoundError:
        print('Error: Build file cannot be found. Please check if the path is valid.\n')
        sys.exit()
    if args.input[0] != 'b':
        print('Warning: Tape to process did not have a blank (b) as its first character. Blank will be prepended automatically.')
    if error:
        sys.exit()
    return args
