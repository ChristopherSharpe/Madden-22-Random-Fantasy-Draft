import random
import csv

f = open("MaddenFile.txt", "w") # JOSH - should be in a function probably. 
#Created the team and position lists
team_list = ["Cardinals", "Falcons", "Panthers", "Ravens", "Bills", "Bears", "Bengals", "Browns", "Cowboys", "Broncos", "Lions", "Packers", "Texans", "Colts", "Jaguars", "Chiefs", "Raiders", "Chargers", "Rams", "Dolphins", "Vikings", "Patriots", "Saints", "Giants", "Jets", "Eagles", "Steelers", "49ers", "Seahawks", "Buccaneers", "Titans", "Commanders" ]
position_list = ["QB", "RB", "WR", "FB", "TE", "LT", "RT", "LG", "RG", "C", "DT", "DE", "MLB", "LOLB", "ROLB", "CB", "FS", "SS", "K", "P"]

#Creating dicts and lists to be used throughout the program 
# JOSH - try to get rid of all thees below. Use function parameters and return statements. Not globals.
num_rounds = []
num_picks = {}
name_and_team_dict = {}
number_of_teams = []
number_of_users_list = []
team_for_each_user = []

# JOSH - Each function should do exactly one thing. This function shouldn't write to a file. It should return a list. You also want a second function that does the stuff inside the for loop. You never want to write a file this way though. You want to open, write, and close a file as soon as possible. Not leave it open.
# Creating a function to give users a random team from team list, and writing it to a file, will convert to a csv file soon
def randomTeamForUsers():
    number_of_users = int(input ("How many players will there be: ")) # JOSH - pass this value in as parameter. Don't collect here.
    #For I in the range of number of users that are entered to play.(User enters a number of players)
    for i in range(number_of_users):
        userName = (input ("Name of user: ")) # JOSH - even better, ignore my comment on 20 and pass in an array of usernames. 
        num_of_each_user = 1 # JOSH - what is this? 
        rand_Team = random.choice(team_list)
        team_list.remove(rand_Team)
        name_and_team = userName + " : " + rand_Team + " "
        name_and_team_dict[name_and_team] = num_of_each_user
        number_of_teams = int(number_of_users) # JOSH - What are you trying to do here?
        number_of_users_list.append(number_of_users) # JOSH - What are you trying to do here?
        team_for_each_user.append(name_and_team) # JOSH - What are you trying to do here?
        f.write(name_and_team) # JOSH - Return list once you are finished with for loop, don't write to file.
    



        

#Creates the function to determine how many rounds to be picked, and how many of each position will be picked. 
def calculate_rounds():
    for key in range(len(position_list)):
        key = position_list[key]
        num_pos = int(input("How many " + key + "s would you like to draft: ")) # JOSH - The problem with asking for input inside functions is that you can't change it to read from file or anything else later easily. Always try to pass input into function as parameter so it can change.
        num_picks[key] = num_pos
        num_rounds.append(num_pos)
    print(f"You will draft for a total of {sum(num_rounds)} rounds") # JOSH - you should return this value, don't use a global array

#Creating the randomizer to randomly give users positions to pick each round. 

def randomized_postions():
    picks_for_each_round = []
    key = 1
    rounds = sum(num_rounds) # JOSH - I'm confused here. Won't this mean that different teams have different number of rounds? Shouldn't each team get X rounds (same for all) that they then allocate for each positions?
    #While rounds doesn't equal 0, this should continue
    while rounds != 0:
        round_counter ="Round: ", key    # JOSH - counter shouldn't have string, just number.
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
                           
def main(): #passed through as a paramater # JOSH - What does this comment mean?
    number_of_users = len(team_for_each_user)
    picks = []
    name_of_user_and_picks = {}
    picks.append(randomized_postions())
    print(number_of_users)
    print(name_and_team_dict.items())
    print(picks)
    
    # JOSH - you are trying to do too much at once. Make smaller, testable steps. For a draft, you have to do the following. Each of these should be at least one separate function. It'll help clean up the below code. I'm honestly unsure what you are trying to do in it.
    # 1. Determine which users are invovled
    # 2. Assign each user an NFL team, the remaining NFL teams should get excluded? Or given a "CPU" spot that gets auto-drafted?
    # 3. Each user should determine their position breakdown - if there are 56 total rounds (I think that's the NFL roster size), they should start with 56 spots that they allocate to positions. This may not be necessary. Maybe each user wants to draft whatever they want (12 kickers on a team?)
    # 4. Determine draft order. Depends on how you want to do it. NFL has same order each round. You can make each round random. I think this is what you are trying to do below. Don't try to select pick and determine draft order same time. Do one, then once it's in an array, you can just loop through.
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
