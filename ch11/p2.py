class animal:
    pass

class pets(animal):
    pass

class dogs(pets):
    def bark():
        print("Bow Bow!")

d = dogs
d.bark()
