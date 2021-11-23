import unittest
from unittest.case import expectedFailure
from src.bus import Bus
from src.bus_stop import BusStop
from src.person import Person

class TestBus(unittest.TestCase):
    def setUp(self):
        self.bus = Bus(22, "Ocean Terminal", 2, 5)

    # @unittest.skip("Delete this line to run the test")
    def test_has_route_number(self):
        self.assertEqual(22, self.bus.route_number)


    # @unittest.skip("Delete this line to run the test")
    def test_has_destination(self):
        self.assertEqual("Ocean Terminal", self.bus.destination)

    # @unittest.skip("Delete this line to run the test")
    def test_has_price(self):
        self.assertEqual(2, self.bus.price)

    # @unittest.skip("Delete this line to run the test")
    def test_has_capacity(self):
        self.assertEqual(5, self.bus.capacity)

    # @unittest.sk
    # ip("Delete this line to run the test")
    def test_can_drive(self):
        self.assertEqual("Brum brum", self.bus.drive())

    # @unittest.skip("Delete this line to run the test")
    def test_starts_with_no_passengers(self):
        self.assertEqual(0, self.bus.passenger_count())

    # @unittest.skip("Delete this line to run the test")
    def test_can_pick_up_passenger(self):
        person = Person("Guido van Rossum", 64, 20, "Ocean Terminal")
        self.bus.pick_up(person)
        self.assertEqual(1, self.bus.passenger_count())

    # @unittest.skip("Delete this line to run the test")
    def test_can_drop_off_passenger(self):
        person = Person("Guido van Rossum", 64, 20, "Ocean Terminal")
        self.bus.pick_up(person)
        self.bus.drop_off(person)
        self.assertEqual(0, self.bus.passenger_count())

    # @unittest.skip("Delete this line to run the test")
    def test_can_empty_bus(self):
        person = Person("Guido van Rossum", 64, 20, "Ocean Terminal")
        self.bus.pick_up(person)
        self.bus.empty()
        self.assertEqual(0, self.bus.passenger_count())

    def test_bus_fare_paid(self):
        person = Person("Guido van Rossum", 64, 20, "Ocean Terminal")
        expected = 2
        self.bus.pay_fare(person)
        result = self.bus.fare_cash
        self.assertEquals(expected, result)

    def test_bus_fare_taken(self):
        person = Person("Guido van Rossum", 64, 20, "Ocean Terminal")
        expected = 18
        self.bus.pay_fare(person)
        result = person.cash
        self.assertEquals(expected, result)

    # @unittest.skip("Delete this line to run the test")
    def test_can_pick_up_passenger_from_bus_stop(self):
        person_1 = Person("Guido van Rossum", 64, 20, "Ocean Terminal")
        person_2 = Person("Carol Willing", 50, 50, "Lothian Road")
        bus_stop = BusStop("Waverly Station")
        bus_stop.add_to_queue(person_1)
        bus_stop.add_to_queue(person_2)
        self.bus.pick_up_from_stop(bus_stop)
        self.assertEqual(1, self.bus.passenger_count())
        self.assertEqual(2, self.bus.fare_cash)
        self.assertEqual(18, person_1.cash)
        self.assertEqual(1, bus_stop.queue_length())
        
