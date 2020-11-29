from myassembler import assemble
from myargparser import parser
from state import State
from turing_mach import TM

args = parser()
tm = assemble(args.build)
tm.load_tape(args.input)
print(tm.process())