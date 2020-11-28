
from pylint.lint import Run

results = Run(['state.py'], do_exit=False)
# `exit` is deprecated, use `do_exit` instead
print(results.linter.stats['global_note'])