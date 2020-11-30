''' Main script that uses TM and State obj to simulate TM behavior '''
from myassembler import assemble
from myargparser import parser

args = parser()
tm = assemble(args.build)
tm.load_tape(args.input)
print(tm.process())
