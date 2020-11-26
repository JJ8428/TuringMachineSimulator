''' Simple argparser '''
import argparse
import sys

def argp():
    ''' Simple parser to check build, input, and output path '''
    # 3 arguments: build, input, output
    # build is a file with the states defined
    # input is a file where the string(s) are taking as input
    # output is a file where the processed string(s) are saved
    parser = argparse.ArgumentParser(description='Simulate the behavior of a Turing Machine')
    parser.add_argument('-b', '--build', type=str, metavar='', required=True,
                        help='Path of file containing Turing Machine build')
    parser.add_argument('-i', '--input', type=str, metavar='', required=True,
                        help='Path of file containing strings to process')
    parser.add_argument('-o', '--output', type=str, metavar='', required=True,
                        help='Path of file to write processed strings into')
    args = parser.parse_args()
    # Check if paths are valid files
    error = False
    try:
        r = open(args.build, 'r')
        r.close()
    except Exception:
        print('Error: Build file cannot be found. Please check if the path is valid.\n')
        error = True
    try:
        r = open(args.input, 'r')
        r.close()
    except Exception:
        print('Error: Build file cannot be found. Please check if the path is valid.\n')   
        error = True
    try:
        r = open(args.output, 'r')
        r.close()
    except Exception:
        print('Error: Build file cannot be found. Please check if the path is valid.\n')
        error = True
    if error:
        sys.exit()
    return args