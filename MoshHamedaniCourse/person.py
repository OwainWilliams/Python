class Person:
    def __init__(self, name): #careful not to put too many underscores in! 
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("Owain Williams")
john.talk()

bob = Person("Bob Smith")
bob.talk()