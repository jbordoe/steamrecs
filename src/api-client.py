#!/usr/bin/env python3

from src import steamapi

__author__ = 'soheb'

import argparse

# somoso's profile
defaultSteamID = 76561197983149697

parser = argparse.ArgumentParser(description="Steam API implemented in Python")
parser.add_argument('--steamID', dest='steamID', help="The steam ID in 64 bit format")
argument = parser.parse_args()

steamID = defaultSteamID
if argument.steamID:
    steamID = argument.steamID

key = steamapi.getsteamkey()

print("Fetching data about user " + steamID)
result = steamapi.getownedgames(key, steamID)
if result is None:
    print("Failure in getting data, probably because of dud steam ID")
else:
    print(steamapi.getownedgames(key, steamID))