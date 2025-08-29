class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Swim faster")

    def swim(self):
        print("Swim faster")

class Penguin(Bird):

    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run (self):
        print("Run faster")

peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
