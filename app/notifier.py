from is_online import is_online
from send_sms import send_sms

# Players to get notified on
playerids = [""]

while True:
    for playerid in playerids:
        if is_online(playerid):
            print(f"Player {playerid} is online")
            send_sms(playerid)
            playerids.remove(playerid)
        elif is_online(playerid)!=True:
            playerids.append(playerid)
        else:
            pass
