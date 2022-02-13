import random
import csv

f = open("MaddenFile.txt", "w")
#Created the team and position lists
team_list = ["Cardinals", "Falcons", "Panthers", "Ravens", "Bills", "Bears", "Bengals", "Browns", "Cowboys", "Broncos", "Lions", "Packers", "Texans", "Colts", "Jaguars", "Chiefs", "Raiders", "Chargers", "Rams", "Dolphins", "Vikings", "Patriots", "Saints", "Giants", "Jets", "Eagles", "Steelers", "49ers", "Seahawks", "Buccaneers", "Titans", "Commanders" ]
position_list = ["QB", "RB", "WR", "FB", "TE", "LT", "RT", "LG", "RG", "C", "DT", "DE", "MLB", "LOLB", "ROLB", "CB", "FS", "SS", "K", "P"]

#Creating dicts and lists to be used throughout the program 
num_rounds = []
num_picks = {}
name_and_team_dict = {}
number_of_teams = []
number_of_users_list = []
team_for_each_user = []
# Creating a function to give users a random team from team list, and writing it to a file, will convert to a csv file soon
def randomTeamForUsers():
    number_of_users = int(input ("How many players will there be: "))
    #For I in the range of number of users that are entered to play.(User enters a number of players)
    for i in range(number_of_users):
        userName = (input ("Name of user: "))
        num_of_each_user = 1
        rand_Team = random.choice(team_list)
        team_list.remove(rand_Team)
        name_and_team = userName + " : " + rand_Team + " "
        name_and_team_dict[name_and_team] = num_of_each_user
        number_of_teams = int(number_of_users)
        number_of_users_list.append(number_of_users)
        team_for_each_user.append(name_and_team)
        f.write(name_and_team)
    



        

#Creates the function to determine how many rounds to be picked, and how many of each position will be picked. 
def calculate_rounds():
    for key in range(len(position_list)):
        key = position_list[key]
        num_pos = int(input("How many " + key + "s would you like to draft: "))
        num_picks[key] = num_pos
        num_rounds.append(num_pos)
    print(f"You will draft for a total of {sum(num_rounds)} rounds")

#Creating the randomizer to randomly give users positions to pick each round. 

def randomized_postions():
    picks_for_each_round = []
    key = 1
    rounds = sum(num_rounds)
    #While rounds doesn't equal 0, this should continue
    while rounds != 0:
        round_counter ="Round: ", key    
        #Creates a variable for the random position to be chosen from the position list
        random_position_choice = random.choice(position_list)
        for keys, values in num_picks.items():
            #If the key from the num_picks dict is equal to random_position_choice(random position chosen from list) and if value from the Key:Value pair in num_picks doesn't equal 0: value - 1 and key + 1 
            if keys == random_position_choice and values != 0:
                num_picks[keys] = values - 1
                key = key + 1
                rounds = rounds - 1 
                picks_for_each_round.append(random_position_choice)
            else:
                continue
    return picks_for_each_round
                           
def main(): #passed through as a paramater
    number_of_users = len(team_for_each_user)
    picks = []
    name_of_user_and_picks = {}
    picks.append(randomized_postions())
    print(number_of_users)
    print(name_and_team_dict.items())
    print(picks)
    while number_of_users != 0:
        random_team = random.choice(team_for_each_user)
         # this is how I am trying to call the function, I don't know if this is allowed.
        for name_and_team, num_of_each_user in name_and_team_dict.items():
            if name_and_team == random_team and num_of_each_user != 0:           
                print("We made it here too!")
                name_and_team_dict[name_and_team] = num_of_each_user - 1
                number_of_users = number_of_users - 1
                name_of_user_and_picks[random_team] = random.shuffle(picks)       
            else:
                continue
    print(name_of_user_and_picks)   

                
                  
    


randomTeamForUsers()
calculate_rounds()
main() 


f.close()