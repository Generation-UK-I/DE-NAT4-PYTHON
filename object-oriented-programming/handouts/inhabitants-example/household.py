from cat import Cat
from person import Person
from typing import List
from inhabitant import Inhabitant

inhabitants = [Cat('Gera', 9), Person('Dmitry', 24)]

def do_all_the_things(inhabitants: List[Inhabitant]):
    
    print('\n')
    
    for inhabitant in inhabitants:
        
        print(inhabitant)
        
        inhabitant.pay_bills()
        
        try:
            inhabitant.eat()
        except:
            print(f'{inhabitant.name} does not inherit from class Animal and does not have .eat() method')
        
        print('\n')
        
do_all_the_things(inhabitants)
