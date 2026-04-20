class Inhabitant():
    
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        
    #Overides __str__() function from Python Object class, this allows to print custom string when printing the class
    def __str__(self, inhabitant_type) -> str:
        return f'Hi my name is {self.name}. I am {self.age} years old. I am a {inhabitant_type}'
    
    def pay_bills(self) -> None:
        print(f'{self.name} has paid the bills this month')
        