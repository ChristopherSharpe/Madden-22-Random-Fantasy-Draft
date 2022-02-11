import random
import csv

f = open("MaddenFile.txt", "w")
#Created the team and position lists
team_List = ["Cardinals", "Falcons", "Panthers", "Ravens", "Bills", "Bears", "Bengals", "Browns", "Cowboys", "Broncos", "Lions", "Packers", "Texans", "Colts", "Jaguars", "Chiefs", "Raiders", "Chargers", "Rams", "Dolphins", "Vikings", "Patriots", "Saints", "Giants", "Jets", "Eagles", "Steelers", "49ers", "Seahawks", "Buccaneers", "Titans", "Commanders" ]
position_list = ["QB", "RB", "WR", "FB", "TE", "LT", "RT", "LG", "RG", "C", "DT", "DE", "MLB", "LOLB", "ROLB", "CB", "FS", "SS", "K", "P"]

#Creating dicts to use for number of rounds to be picked, and the number of picks per position, which will be entered by user. 
numRounds = []
numPickPerPos = {}

#Creating a function to give users a random team from team list, and writing it to a file, will convert to a csv file soon
def randomTeamForUsers():
    numOfUsers = int(input ("How many players will there be: "))
    f = open("MaddenFile.txt", "w")
    #For I in the range of number of users that are entered to play.(User enters a number of players)
    for i in range(numOfUsers):
        userName = (input ("Name of user: "))
        rand_Team = random.choice(team_List)
        team_List.remove(rand_Team)
        nameAndTeam = userName + " : " + rand_Team + " "
        print(nameAndTeam)
        print(team_List)
        f.write(nameAndTeam)


#Creates the function to determine how many rounds to be picked, and how many of each position will be picked. 
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

#Creating the randomizer to randomly give users positions to pick each round. 
def randomizedPositions():
    pickForEachRound = {}
    rounds = sum(numRounds)
    key = 1
    
    #While rounds doesn't equal 0, this should continue
    while rounds != 0:
        newKey ="Round: ", key 
        
        #Creates a variable for the random position to be chosen from the position list
        posKeys = random.choice(position_list)
        
        for keys, values in numPickPerPos.items():
            #If the key from the numPickPerPos dict is equal to posKeys(random position chosen from list) and if value from the Key:Value pair in numPickPerPos doesn't equal 0: value - 1 and key + 1 
            if keys == posKeys and values != 0:
                    numPickPerPos[keys] = values - 1
                    key = key + 1
                    rounds = rounds - 1
                    pickForEachRound[newKey] = posKeys
            else:
                continue
                    
                        
    
             
        
        
            
                
    
    print(pickForEachRound)
    print(numPickPerPos)
                  
    


randomTeamForUsers()
numOfRounds()
randomizedPositions()


f.close()