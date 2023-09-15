
STUDENTS=["Alice","Bob","Charlie","David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
PLANTS={"C":"Clover", "G":"Grass","R":"Radishes","V":"Violets"}


class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.diagram=diagram.split("\n")
        self.students=sorted(students) 
               
                   
        
    def plants(self,st_name):
        students_seeds={}
        index=0
        row1,row2=self.diagram    
        for n in range(0,len(self.students)*2,2):        
            couple=[row1[n:n+2:],row2[n:n+2:]]      
            students_seeds[self.students[index]]= [PLANTS[seed] for seeds in couple for seed in seeds]
            index+=1
    
        return students_seeds[st_name]
                