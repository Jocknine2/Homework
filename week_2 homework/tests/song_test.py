import unittest
from src.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("battery", "Metallica")

    def test_song_has_title(self):
        self.assertEqual("battery", self.song.title)
