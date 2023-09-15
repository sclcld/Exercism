ALLERGENS={
    1:"eggs",
    2:"peanuts", 
    4:"shellfish", 
    8:"strawberries",
    16:"tomatoes",
    32:"chocolate",
    64:"pollen", 
    128:"cats"} 




class Allergies:
    def __init__(self, score):
        self.score=score

    def allergic_to(self, item):
        return item in self.lst

    @property
    def lst(self):
        return [allergen for value,allergen in ALLERGENS.items() if self.score&value]
