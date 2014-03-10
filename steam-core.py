__author__ = 'soheb'

# For good documentation procedure when commenting
# http://legacy.python.org/dev/peps/pep-0257/

import urllib.request, argparse, sys

defaultSteamID = 76561197983149697

def main():

    parser = argparse.ArgumentParser(description="Does something interesting with your steam details. Don't really know yet")
    parser.add_argument('--steamid', dest='steamID')
    argument = parser.parse_args()

    # somoso's profile
    steamID = defaultSteamID
    if argument.steamID:
        steamID = argument.steamID

    key = getKey()

    getOwnedGames(key, steamID)

""" Return parsed JSON data of all owned games by the steam ID """
def getOwnedGames(key, steamID):
    url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" + str(key) + "&steamid=" + str(steamID) + "&include_appinfo=1&include_played_free_games=1"
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
    except urllib.request.HTTPError as error:
        data = error.read()
    print(data.decode('utf-8'))


""" Return the steam key found in the same directory as this code """
def getKey():
    steamKeyFile = open('steamkey', 'r')
    key = steamKeyFile.readline()
    steamKeyFile.close()
    return key.rstrip('\n')

if __name__ == "__main__":
    main()