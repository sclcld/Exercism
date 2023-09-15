
SHARP_CHR=["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
FLAT_CHR=["F", "Gb", "G", "Ab", "A", "Bb", "B", "C", "Db", "D", "Eb", "E"]
SHARPS=["C","G", "D", "A", "E", "B", "F#", "a" , "e", "b", "f#", "c#", "g#", "d#"]
FLATS=["F", "Bb", "Eb", "Ab", "Db", "Gb","d","g", "c", "f", "bb", "eb"]


class Scale:
    def __init__(self, tonic):
        self.tonic=tonic
        self.chrm=self.chromatic()

    def chromatic(self):
        scale=SHARP_CHR if self.tonic in SHARPS else FLAT_CHR
        scale=scale[scale.index(self.tonic.capitalize()):]+scale[:scale.index(self.tonic.capitalize())]
        return scale
    
    def interval(self, intervals):
        dia={"m":1,"M":2,"A":3}
        count=0
        grades=[self.tonic.capitalize()]
        for interval in intervals[:-1]:
            count+=dia[interval[0]]
            grades.append(self.chrm[count])
        grades.append(self.tonic.capitalize())
        return grades
