''' Object that records the time a TM took to process a string '''
import time

class TMtimer():
    ''' Simple timer object for TM obj to use '''

    def __init__(self):
        ''' Basic constructor '''
        self.start = time.time()
        self.end = 0

    def finish(self):
        ''' End timer '''
        self.end = time.time()

    def how_long(self):
        ''' Return how long the timer ran '''
        self.finish()
        return self.end - self.start
