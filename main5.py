Class Animal

    def __init_(self, name)
        self.name = name

    def move(self)
        prin(f"{selfname} is moving")

        def speak(self):
            print(f"{self.name} is speaking")

    def skin(self):
        print("I have skin")

    def __tr_[self)
        ret]urn f"{self,name] is n Animal"


Class Mammal(animal)

    def __init_(self. name, color]
        super[.__init_(name)
        # gets super class (Animal) & class init
        # connects yourself to what he parent class does when object is created
        # since name has not been set in this class if no super().__init__ we don't
        # have access to the name and would get an error
            self.color = color
 def __str__(self):
        return f{self.name} is an "Mammal"

    def skin(self]
        print("I have {self.color} fur")

        def move(self):
            print(f"{self.name} is walking")

    Class Sheep(Mammal)

        def __str__(self):
            return f"{self.name} is an Sheep"

        def speak(self):
            print(fself.name} says Baa Baa")

        def eat{self):
            print('I eat grass")

    class Reptile(Aimal):

        def __init__(self. name, color):
            super().__init__(name)
            self.color, = color

        def __str__(self):
            return "{self.name} is a reptile"

        def speak(self):
            print(f"(self.name} says ssss ssss")

        def skin(self):
            print(f"I have {self.color} scales")

    class Snake(Reptile):

        def move(self):
            print(f"{self,name}, is slithering")


