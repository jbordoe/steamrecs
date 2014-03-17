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

    def getownedgames(self, steamID, includeappinfo = 1,includeplayedf2p = 1, fmt="json"):
        """ Return parsed JSON data of all owned games by the steam ID """
        url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + str(self.key) + "&steamid=" + str(steamID) + "&include_appinfo=" + str(includeappinfo) + "&include_played_free_games=" + str(includeplayedf2p) + "&format=" + fmt
        return self.parseResponse(url)

    def parseResponse(self, url):
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


    def getnews(self, appid=None, count=3, maxlength=300, fmt="json"):
        url = "http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid=" + str(appid) + "&count=" + str(count) + "&maxlength=" + str(maxlength) + "&format=" + str(fmt)
        return self.parseResponse(url)

    def getglobalachievements(self, gameid, fmt="json"):
        url = "http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?gameid=" + str(gameid) + "&format=" + str(fmt)
        return self.parseResponse(url)

    def getplayersummaries(self, steamIDList, fmt="json"):
        steamIDs = ",".join([str(id) for id in steamIDList])
        url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=" + self.key + "&steamids=" + steamIDs + "&format=" + fmt
        return self.parseResponse(url)

    def getfriendlist(self, steamid, relationship="friend", fmt="json"):
        url = "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=" + self.key + "&steamid=" + str(steamid) + "&relationship=" + relationship + "&format=" + fmt
        return self.parseResponse(url)

    def getplayerachievements(self,steamid, appid,lang=None):
        url = "http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid=" + str(appid) + "&key=" + self.key + "&steamid=" + str(steamid);
        if lang is not None:
            url += "&lang=" + lang
        return self.parseResponse(url)

    def getusergamestats(self, steamid, appid, lang=None):
        url = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?appid=" + str(appid) + "&key=" + self.key + "&steamid=" + str(steamid)
        if lang is not None:
            url += "&lang=" + lang
        return self.parseResponse(url)

    def getrecentplayedgames(self,steamid,count=None, fmt="json"):
        raise NotImplementedError

    def isplayingsharedgame(self, steamid, appid, fmt="json"):
        raise NotImplementedError

def getsteamkey():
    """ Return the steam key found in the same directory as this code """
    steamKeyFile = open(os.path.dirname(os.path.realpath(__file__)) + '/steamkey', 'r')
    key = steamKeyFile.readline()
    steamKeyFile.close()
    return key.rstrip('\n')