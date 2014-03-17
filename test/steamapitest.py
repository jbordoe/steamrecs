#!/usr/bin/env python3

from src import steamapi
from src.steamapi import SteamApi

__author__ = 'soheb'

import unittest


class SteamAPITestCase(unittest.TestCase):

    def setUp(self):
        self.steam = SteamApi(steamapi.getsteamkey())

    def test_getownedgames_fail(self):
        self.assertIsNone(self.steam.getownedgames(0))

    def test_getownedgames_success(self):
        self.assertIsNotNone(self.steam.getownedgames(76561197983149697))

    def test_getnews_fail(self):
        self.assertIsNone(self.steam.getnews(-1))

    def test_getnews_success(self):
        self.assertIsNotNone(self.steam.getnews(440))

    def test_getglobalachievements_fail(self):
        self.assertIsNone(self.steam.getglobalachievements(-1))

    def test_getglobalachievements_success(self):
        self.assertIsNotNone(self.steam.getglobalachievements(440))

    def test_getplayersummaries_fail(self):
        self.assertEqual(self.steam.getplayersummaries([-1,-2,-3]), {'response': {'players': []}})

    def test_getplayersummaries_success(self):
        self.assertIsNotNone(self.steam.getplayersummaries([76561197983149697,76561197983149697]))

    def test_getusergamestats_fail(self):
        self.assertIsNone(self.steam.getusergamestats(-1,-1))

    def test_getusergamestats_success(self):
        self.assertIsNotNone(self.steam.getusergamestats(76561197983149697, 440))

    def test_getrecentplayedgames_fail(self):
        self.assertIsNone(self.steam.getrecentplayedgames(-1))

    def test_getrecentplayedgames_success(self):
        self.assertIsNotNone(self.steam.getrecentplayedgames(76561197983149697))

    def test_isplayingsharedgame_fail(self):
        self.assertIsNone(self.steam.isplayingsharedgame(-1,-1))

    def test_isplayingsharedgame_success(self):
        self.assertIsNotNone(self.steam.isplayingsharedgame(76561197983149697,440))

if __name__ == '__main__':
    unittest.main()
