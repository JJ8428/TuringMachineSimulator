''' Pyscript to score files '''
from pylint.lint import Run

results = Run(['timer.py'], do_exit=False)
print(results.linter.stats['global_note'])