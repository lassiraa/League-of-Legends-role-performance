import requests
import re

api_key = ""  # your API key here
summoner_name = input("Enter summoner name: ")
url = "https://euw1.api.riotgames.com/lol/summoner/v3/summoners/by-name/" + summoner_name + "?api_key=" + api_key
summoner_page = requests.get(url)
summoner_page = str(summoner_page.content)
account_id = summoner_page[30:39]
url = "https://euw1.api.riotgames.com/lol/match/v3/matchlists/by-account/" + account_id + "?queue=420&season=11&api_key=" + api_key
match_history = str((requests.get(url)).content)
roles = re.findall(r'"role":"(.*?)","', match_history)
lanes = re.findall(r'"lane":"(.*?)"}', match_history)
i = 0
what_role = []
for lane in lanes:
    if lanes[i] == "JUNGLE" and roles[i] == "NONE":
        what_role.append("JUNGLE")
    elif lanes[i] == "NONE" and roles[i] == "DUO_SUPPORT":
        what_role.append("SUPPORT")
    elif lanes[i] == "MID":
        what_role.append("MID")
    elif lanes[i] == "TOP":
        what_role.append("TOP")
    elif lanes[i] == "BOTTOM":
        what_role.append("ADC")
    else:
        what_role.append("REMAKE")
    i+=1
print(what_role)  # prints the amount of games you have on each role