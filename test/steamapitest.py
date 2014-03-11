#!/usr/bin/env python3

from src import steamapi
from src.steamapi import SteamApi

__author__ = 'soheb'

import unittest


class SteamAPITestCase(unittest.TestCase):

    def setUp(self):
        self.steam = SteamApi(steamapi.getsteamkey())

    def test_fake_user(self):
        self.assertIsNone(self.steam.getownedgames(0))

    def test_success(self):
        self.assertIsNotNone(self.steam.getownedgames(76561197983149697))


if __name__ == '__main__':
    unittest.main()
