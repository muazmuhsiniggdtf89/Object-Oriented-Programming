# Parent class
class dad:

    def __init__(self, eyes, aggressive):
        self.eyes = eyes
        self.aggressive = aggressive

    def display(self):
        print("Your eye color is", self.eyes)
        print("You are aggressive", self.aggressive)

# child class
class son (dad):

    def __init__(self, name, age, eyes, aggressive):
        self.name = name 
        self.age = age 
         
         #invoking the _init_ of parent class
         # to access its attributes
        dad.__init__(self, eyes, aggressive)

# object creation 
obj = son ("Penguin", 8, "blue", True)

# callaing method display 
obj.display()

