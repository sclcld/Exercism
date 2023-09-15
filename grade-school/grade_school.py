class School:
    
    def __init__(self):
        self.school={}
        self._added=[]

    def add_student(self, name, grade):
        students=[student for group in [self.school[key] for key in self.school] for student in group]
        if name in students:
            self._added.append(False)
        else:
            if grade in self.school:
                self.school[grade].append(name)
            else:
                self.school[grade]=[name]             
            self._added.append(True)         
    
    def roster(self):
        return [name for grades in sorted(self.school) for name in self.grade(grades)]         
           
    def grade(self, grade_number):       
        if grade_number in self.school.keys():
            return sorted(self.school[grade_number])
        return []

    
    def added(self):
        return self._added
