class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.destination = destination
        self.price = price
        self.capacity = capacity
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, person):
        if person in self.passengers:
            self.passengers.remove(person)

    def empty(self):
        self.passengers = []