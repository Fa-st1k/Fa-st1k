class Person:

    def __init__(self, name):
        self.name = name  # имя человека
        self.age = 1  # возраст человека

tom = Person("Gerry")
print(tom.name)
tom.age = 31
print(tom.age)