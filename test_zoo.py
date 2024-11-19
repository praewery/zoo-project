import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_negativeage_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), "Don't have negative age")

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50)
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(14), 100)
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    def test_adult_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
        self.assertEqual(self.zoo.get_ticket_price(60), 150)

    def test_elder_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
       

if __name__ == '__main__':
    unittest.main()