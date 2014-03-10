__author__ = 'soheb'

# For good documentation procedure when commenting
# http://legacy.python.org/dev/peps/pep-0257/

import urllib.request
import argparse
import json

# somoso's profile
defaultSteamID = 76561197983149697

def main():
    parser = argparse.ArgumentParser(description="Steam API implemented in Python")
    parser.add_argument('--steamID', dest='steamID', help="uses provided steam ID instead of default one")
    argument = parser.parse_args()

    steamID = defaultSteamID
    if argument.steamID:
        steamID = argument.steamID

    key = getKey()

    print(getOwnedGames(key, steamID))

def getOwnedGames(key, steamID):
    """ Return parsed JSON data of all owned games by the steam ID """
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + str(key) + "&steamid=" + str(steamID) + "&include_appinfo=1&include_played_free_games=1"
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

def getKey():
    """ Return the steam key found in the same directory as this code """
    steamKeyFile = open('steamkey', 'r')
    key = steamKeyFile.readline()
    steamKeyFile.close()
    return key.rstrip('\n')

if __name__ == "__main__":
    main()