import unittest
from src.guest import Guest
from src.room import Room


class TestGuest(unittest.TestCase):
    def setUp(self):

        self.guest = Guest("Dave", 100.00)
        self.room1 = Room(1, 3, 5)

    def test_get_guest_name(self):
        self.assertEqual("Dave", self.guest.name)

    def test_get_wallet(self):
        self.assertEqual(100.00, self.guest.wallet)

    def test_pay_entry_fee(self):
        self.guest.pay_entry_fee(self.room1)
        self.assertEqual(95, self.guest.wallet)
