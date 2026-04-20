from inhabitant import Inhabitant
from animal import Animal

#Inherits from 2 classes; Inhabitant and Animal
class Cat(Inhabitant, Animal):
    inhabitant_type = 'Cat'
    food = 'Cat Food'
    
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        print(f'A new cat named {self.name} has been created and it is {self.age} years old')
        
    def make_sound(self) -> None:
        print(f'{self.name} said Meow!')
    
    def incriment_age(self) -> None:
        self.age += 1
    
    #Overides pay_bills() function from Inhabitants
    def pay_bills(self) -> None:
        print('How dare you ask me to the bills... you peasant human')
    
    #Overides __str__() function from Python Object class, this allows to print custom string when printing the class
    def __str__(self) -> str:
        return super().__str__(self.inhabitant_type)

