import requests

# API Keys generated from https://developer.riotgames.com

def requestSummonerData(summonerName, APIKey):
    # URL Creation
    URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summonerName + "?api_key=" + APIKey
    # Obtain JSON information
    response = requests.get(URL)
    # Print URL generated -> Testing Purposes
    print("\n" + "requestSummonerData URL: " + URL)
    return response.json()

def requestRankedData(encryptedSummonerId, APIKey):
    URL = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + encryptedSummonerId + "?api_key=" + APIKey
    response = requests.get(URL)
    # Print URL generated -> Testing Purposes
    print("\n" + "requestRankedData URL: " + URL + "\n")
    return response.json()

def main():
    summonerName = input('Enter your summoner Name: ')
    APIKey = input('Enter your APIKey: ')

    # Format summoner name for OP.GG
    newSummonerName = summonerName.replace(" ", "+")
    summonerURL = "https://na.op.gg/summoner/userName=" + newSummonerName

    # Get Summoner Data using summonerName and API Key
    responseJSON = requestSummonerData(summonerName, APIKey)

    # Override summonerName via input in case they didn't put capitals in their name
    summonerName = responseJSON['name']
    summonerLevel = str(responseJSON['summonerLevel'])
    encryptedSummonerId = responseJSON['id']

    # Get ranked information only if they are able to play ranked (must be level 30 or higher for ranked games)
    if (int(summonerLevel) >= 30):
        # Get Ranked Information on the account using Encryed Summoner ID and API Key
        responseJSONRankedData = requestRankedData(encryptedSummonerId, APIKey)
        summonerTier = responseJSONRankedData[0]['tier']
        summonerRank = responseJSONRankedData[0]['rank']
        summonerLP = responseJSONRankedData[0]['leaguePoints']

        print(f"Ranked Data was found...\n\nSummoner Name: {summonerName}\nSummoner Level: {summonerLevel}\nSummoner Tier: {summonerTier}\nSummoner Rank: {summonerRank}\nSummoner LP: {summonerLP}\nOP.GG: {summonerURL}\n")
    else:
        print(f"\nRanked Data cannot be found...\n\nData Found:\nSummoner Name: {summonerName}\nSummoner Level: {summonerLevel}")

if __name__ == "__main__":
    main()
