''' fsd '''
import argparse

parser = argparse.ArgumentParser(description='Simulate the behavior of a Turing Machine')
parser.add_argument('-b', '--build', type=str, metavar='', required=True,
                    help='Path of file containing Turing Machine build')
parser.add_argument('-i', '--input', type=str, metavar='', required=True,
                    help='Path of file containing string to process')
parser.add_argument('-o', '--output', type=str, metavar='', required=True,
                    help='Path of file to write processed strings into')
args = parser.parse_args()
print(args.