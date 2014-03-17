#!/usr/bin/env python3

__author__ = 'soheb'

# For good documentation procedure when commenting
# http://legacy.python.org/dev/peps/pep-0257/

import urllib.request
import os
import json

class SteamApi:
    """ A Python implementation of the following API:
        https://developer.valvesoftware.com/wiki/Steam_Web_API
    """

    def __init__(self, key):
        self.key = key

    def getownedgames(self, steamID, includeappinfo = 1,includeplayedf2p = 1, format="json"):
        """ Return parsed JSON data of all owned games by the steam ID """
        url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + str(self.key) + "&steamid=" + str(steamID) + "&include_appinfo=" + str(includeappinfo) + "&include_played_free_games=" + str(includeplayedf2p) + "&format=" + format
        try:
            response = urllib.request.urlopen(url)
            # unfortunately we cannot just do json.load(response) because urllib is stupid
            # http://stackoverflow.com/a/6862922/617028
            str_response = response.readall().decode('utf-8')
            return json.loads(str_response)
        except urllib.request.HTTPError as error:
            data = error.read().decode('utf-8')
            if "500 Internal Server Error" in data:
                return None

    def getnews(self, appid = None, count = 3, maxlength = 300, format = "json"):
        raise NotImplementedError

    def getglobalachievements(self, gameid, format="json"):
        raise NotImplementedError

    def getplayersummaries(self, steamids, format="json"):
        raise NotImplementedError

    def getfriendlist(self, steamid, relationship="friend", format="json"):
        raise NotImplementedError

    def getplayerachievements(self,steamid, appid,lang=None):
        raise NotImplementedError

    def getusergamestats(self, steamid, appid, lang=None):
        raise NotImplementedError

    def getrecentplayedgames(self,steamid,count=None, format="json"):
        raise NotImplementedError

    def isplayingsharedgame(self, steamid, appid, format="json"):
        raise NotImplementedError

def getsteamkey():
    """ Return the steam key found in the same directory as this code """
    steamKeyFile = open(os.path.dirname(os.path.realpath(__file__)) + '/steamkey', 'r')
    key = steamKeyFile.readline()
    steamKeyFile.close()
    return key.rstrip('\n')