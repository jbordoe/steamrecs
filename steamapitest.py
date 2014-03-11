__author__ = 'soheb'

import unittest
import steamapi


class SteamAPITestCase(unittest.TestCase):
    def test_fake_user(self):
        key = steamapi.getsteamkey()
        self.assertIsNone(steamapi.getownedgames(key, 0))

    def test_fake_key(self):
        self.assertIsNone(steamapi.getownedgames(0,76561197983149697))

    def test_success(self):
        key = steamapi.getsteamkey()
        self.assertIsNotNone(steamapi.getownedgames(key, 76561197983149697))


if __name__ == '__main__':
    unittest.main()
