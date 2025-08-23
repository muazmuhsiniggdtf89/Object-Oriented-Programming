class Employee:
    # Initialize
    def __init__(self,name):
        self.name = name
        print("Employee created")

    def _del_(self):
        print("Destructor called ")  

obj = Employee("Elon")
print(obj.name)
print("Program End...")

del obj
print(obj.name)
