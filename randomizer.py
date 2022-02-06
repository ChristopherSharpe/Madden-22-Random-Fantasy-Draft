import random
f = open("MaddenFile.txt", "w")
team_List = ["Cardinals", "Falcons", "Panthers", "Ravens", "Bills", "Bears", "Bengals", "Browns", "Cowboys", "Broncos", "Lions", "Packers", "Texans", "Colts", "Jaguars", "Chiefs", "Raiders", "Chargers", "Rams", "Dolphins", "Vikings", "Patriots", "Saints", "Giants", "Jets", "Eagles", "Steelers", "49ers", "Seahawks", "Buccaneers", "Titans", "Commanders" ]
def randomTeamForUsers():
    numOfUsers = int(input ("How many players will ther be: "))
    f = open("MaddenFile.txt", "w")
    
    for i in range(numOfUsers):
        userName = (input ("Name of user: "))
        rand_Team = random.choice(team_List)
        team_List.remove(rand_Team)
        nameAndTeam = userName + " : " + rand_Team + " "
        print(nameAndTeam)
        print(team_List)
        f.write(nameAndTeam)

            
        
randomTeamForUsers()
f.close()