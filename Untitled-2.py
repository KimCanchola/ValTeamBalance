def sortPlayers(players):
    updatedPlayers = players
    for i in range(1, len(updatedPlayers)):
        temp = updatedPlayers[i-1]
        j = i - 2
        while j >= 0 and getMMR(updatedPlayers[j], False) > getMMR(temp, False):
            updatedPlayers[j+1] = updatedPlayers[j]
            j = j -1
        updatedPlayers[j+1] = temp
    return updatedPlayers



def getMMR(player, weighted):
    mmr = 0
    if player[1] == "Bronze":
        mmr += 300
    elif player[1] == "Silver":
        mmr += 600
    elif player[1] == "Gold":
        mmr += 900
    elif player[1] == "Plat":
        mmr += 1200
    elif player[1] == "Diamond":
        mmr += 1500
    elif player[1] == "Immortal":
        mmr += 1800
    elif player[1] == "Radiant":
        mmr += 2000

    mmr += player[2] * 100

    if weighted:
        mmr += (int((1 - abs(player[3])) * (player[3]/abs(player[3])) / .05) * 250)
    return mmr



        



if __name__ == "__main__":
    #test case
    players = [["JohnSmith#NA1", "Gold", 2, 1.21 ], ["ter#123", "Bronze", 1, .71],["Test#NA1", "Plat", 2, 1.01 ], 
    ["EEEEEE#123", "Plat", 3, .87],["gon#NA1", "Silver", 1, 1.06 ], ["idk#1s3", "Iron", 3, .71],
    ["ahhhh#123", "Silver", 2, .97],["dsfardg#NA1", "Gold", 3, 1.30 ], ["tuck#no", "Plat", 1, .99],["two#no", "Plat", 3, 1.02]]

    print(sortPlayers(players))

    for i in players:
        print(getMMR(i, True))