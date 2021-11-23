from src.bus_stop import BusStop

class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.destination = destination
        self.price = price
        self.capacity = capacity
        self.passengers = []
        self.fare_cash = 0

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

    def pay_fare(self, person):
        self.fare_cash += self.price
        person.reduce_cash(self.price)

    def remaining_capacity(self):
        return self.capacity - len(self.passengers)

    def pick_up_from_stop(self, bus_stop):
        # passengers_at_stop = bus_stop.get_passengers()
        # self.passengers += passengers_at_stop
        # self.fare_cash += (len(passengers_at_stop) * self.price)
        # bus_stop.clear()
        got_on = []
        for person in bus_stop.queue:
            if self.remaining_capacity() > 0 and person.destination == self.destination:
                self.pay_fare(person)
                self.pick_up(person)
                got_on.append(person)
            
        for person in got_on:
            if person in bus_stop.queue:
                bus_stop.queue.remove(person)

        
