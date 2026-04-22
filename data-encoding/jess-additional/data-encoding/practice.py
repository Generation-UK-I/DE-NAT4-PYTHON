class Cat(): 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.age} the cat can sleep")

    def climb(self):
        print(f"Quick! {self.name} is climbing on the roof!")


my_cat = Cat('Weasley', 2)
my_cat2 = Cat('Noche', 3)

my_cat.sleep()
my_cat.climb()


my_cat2.sleep()
my_cat2.climb()
