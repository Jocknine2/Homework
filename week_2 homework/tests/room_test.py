import unittest
from src.song import Song
from src.room import Room
from src.guest import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 4, 7.50)
        self.guest1 = Guest("John", 15.00)
        self.guest2 = Guest("Barbara", 20.00)
        self.guest3 = Guest("Petunia", 22.00)
        self.guest4 = Guest("Harry", 17.00)
        self.guest5 = Guest("Todd", 6)
        self.song1 = Song("faith", "ghost")
        self.song2 = Song("battery", "Mettalica")
        self.song3 = Song("Horizon", "Cinematic Orchestra")
        self.song4 = Song("reach", "S Club 7")
        self.song5 = Song("Don't stop believing", "Journey")

    def test_get_room_num(self):
        self.assertEqual(1, self.room.room_num)

    def test_get_room_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_get_room_guests(self):
        self.assertEqual(0, self.room.get_guest_count())

    def test_get_room_entry_fee(self):
        self.assertEqual(7.50, self.room.entry_fee)

    def test_check_in_guest_to_room(self):
        self.room.check_in_guest(self.guest1)
        self.assertEqual(1, self.room.get_guest_count())

    def test_check_out_guest_from_room(self):
        self.room.check_in_guest(self.guest3)
        self.room.check_in_guest(self.guest4)
        self.room.check_out_guest(self.guest3)
        self.assertEqual(1, self.room.get_guest_count())

    def test_get_song_count(self):
        self.assertEqual(0, self.room.song_count())

    def test_add_song_to_room(self):
        self.room.add_song(self.song2)
        self.assertEqual(1, self.room.song_count())
