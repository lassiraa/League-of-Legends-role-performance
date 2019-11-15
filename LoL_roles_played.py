import requests
import re

api_key = ""  # your Riot API key here
servers = ["euw1", "eun1", "na1"]
server = input("Enter server (EUW, EUNE, or NA): ")
summoner_name = input("Enter summoner name: ")

if server == "EUW":
    server = servers[0]
elif server == "EUNE":
    sever = servers[1]
else:
    server = servers[2]

url = "https://" + server + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/" + \
      summoner_name + "?api_key=" + api_key
summoner_page = requests.get(url)
account_id = re.findall(r'accountId":"(.*?)","', summoner_page.text)
account_id = account_id[0]

url = "https://euw1.api.riotgames.com/lol/match/v4/matchlists/by-account/" + \
      account_id + "?queue=420&api_key=" + api_key
match_history = (requests.get(url)).text
roles = re.findall(r'"role":"(.*?)","', match_history)
lanes = re.findall(r'"lane":"(.*?)"}', match_history)

roles_play_amount = {
    "Jungle" : 0,
    "Support" : 0,
    "Mid": 0,
    "Adc": 0,
    "Top": 0
}

i=0
for lane in lanes:
    if lane == "JUNGLE" and roles[i] == "NONE":
        roles_play_amount["Jungle"] += 1
    elif lane == "NONE" and roles[i] == "DUO_SUPPORT":
        roles_play_amount["Support"] += 1
    elif lane == "MID":
        roles_play_amount["Mid"] += 1
    elif lane == "TOP":
        roles_play_amount["Top"] += 1
    elif lane == "BOTTOM":
        roles_play_amount["Adc"] += 1
    i+=1

print(roles_play_amount) # prints the amount of games you have in each role
