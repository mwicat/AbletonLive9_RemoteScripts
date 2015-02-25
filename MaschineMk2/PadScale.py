# Source Generated with Decompyle++
# File: PadScale.pyc (Python 2.5)


class PadScale:
    __module__ = __name__
    ''' scale '''
    
    def __init__(self, name, notevalues):
        isinstance(notevalues, tuple)
        self.name = name
        self.notevalues = notevalues
        scale_len = len(self.notevalues)
        rel_range = 16 / scale_len
        self.octave_range = int((10 - rel_range) + 0.5)
        if self.octave_range < 0:
            self.octave_range = 0
        

    
    def to_octave(self, value):
        if self.octave_range == 0:
            return 0
        
        return int(value * self.octave_range)

    
    def to_relative(self, value, prev):
        if self.octave_range == 0:
            return prev
        
        relvalue = value / float(self.octave_range)
        if relvalue > 1:
            return 1
        elif relvalue < 0:
            return 0
        
        return relvalue


