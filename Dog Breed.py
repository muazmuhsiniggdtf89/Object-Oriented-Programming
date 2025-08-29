# create class
class Dog:

    # class attribute
    species = "Dog"

    def __init__(self, breed, age):
        self.breed = breed
        self.age = age

    def display(self):
        print("Species:", Dog.species)
        print("Breed:", self.breed)
        print("Age:", self.age)
        print()


# create objects
dog1 = Dog("German Shepherd", 5)
dog2 = Dog("Labrador Retriever", 3)
dog3 = Dog("Siberian Husky", 4)
dog4 = Dog("French Bulldog", 6)
dog5 = Dog("Border Collie", 7)

# display details
dog1.display()
dog2.display()
dog3.display()
dog4.display()
dog5.display()
