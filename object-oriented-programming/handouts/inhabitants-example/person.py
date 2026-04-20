from inhabitant import Inhabitant

class Person(Inhabitant):
    
    inhabitant_type = 'Human'
    
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        print(f'A new person named {self.name} has been created, and they are {self.age} years old')
    
    #Overides __str__() function from Python Object class, this allows to print custom string when printing the class
    def __str__(self) -> str:
        return super().__str__(self.inhabitant_type)
