class Person:
    def __init__(self, name, age, cash, destination):
        self.name = name
        self.age = age
        self.cash = cash
        self.destination = destination

    def reduce_cash(self, amount):
        self.cash -= amount