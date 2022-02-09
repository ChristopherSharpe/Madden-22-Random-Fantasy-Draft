import random
import csv

f = open("MaddenFile.txt", "w")
team_List = ["Cardinals", "Falcons", "Panthers", "Ravens", "Bills", "Bears", "Bengals", "Browns", "Cowboys", "Broncos", "Lions", "Packers", "Texans", "Colts", "Jaguars", "Chiefs", "Raiders", "Chargers", "Rams", "Dolphins", "Vikings", "Patriots", "Saints", "Giants", "Jets", "Eagles", "Steelers", "49ers", "Seahawks", "Buccaneers", "Titans", "Commanders" ]
position_list = ["QB", "RB", "WR", "FB", "TE", "LT", "RT", "LG", "RG", "C", "DT", "DE", "MLB", "LOLB", "ROLB", "CB", "FS", "SS", "K", "P"]
def randomTeamForUsers():
    numOfUsers = int(input ("How many players will there be: "))
    f = open("MaddenFile.txt", "w")
    
    for i in range(numOfUsers):
        userName = (input ("Name of user: "))
        rand_Team = random.choice(team_List)
        team_List.remove(rand_Team)
        nameAndTeam = userName + " : " + rand_Team + " "
        print(nameAndTeam)
        print(team_List)
        f.write(nameAndTeam)

numRounds = []
numPickPerPos = {}
newNumPickPerPos = {}

def numOfRounds():
    for x in range(len(position_list)):
        keys = position_list[x]
        howManyOfPos = int(input("How many " + keys + "s would you like to draft: "))
        values = int(howManyOfPos)
        numPickPerPos[keys] = values
        numRounds.append(howManyOfPos)
         
    print(numPickPerPos)    
    print(sum(numRounds))
    print("You will draft for a total of ", sum(numRounds), " rounds")


def randomizedPositions():
    pickForEachRound = {}
    rounds = sum(numRounds)
    key = 1
    
    while rounds > 0:
        newKey ="Round: ", key 
        posKeys = random.choice(position_list)
        pickForEachRound[newKey] = posKeys
        rounds = rounds - 1
        key = key + 1
        
        
        
        for keys, values in numPickPerPos.items():
            if keys == posKeys:
                if values != 0:
                    numPickPerPos[keys] = values - 1
                # If the value for random key chosen is 0, return to line 42, or just look for another position with a key whose value > 0
                elif values == 0:
                    Do Something  
                # When all positions have been chosen, break out of loop and contine to next. 
                else:
                    break
    print(pickForEachRound)
    print(numPickPerPos)
                  
    


randomTeamForUsers()
numOfRounds()
randomizedPositions()


f.close()