
class Person:

    def __init__(self, name):#конструктор класса
        self.name = name  # атрибут
        self.age = 1  # возраст человека

    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")


tom = Person(input("Enter your or someone else's name: "))
tom.age = input("Enter your age or someone else's:")
tom.display_info()
print("Congratulations! Now you know your own or someone else's name and age!")







class Person:

    def init(self, name):
        self.name = name  # имя человека
        self.age = 1  # возраст человека

    def display_info(self):
        print(f"Name: {self.name}  Age: {self.age}")


tom = Person("Tom")
tom.age = 37
tom.display_info()  # Name: Tom  Age: 37

bob = Person("Bob")
bob.age = 41
bob.display_info()  # Name: Bob  Age: 41
