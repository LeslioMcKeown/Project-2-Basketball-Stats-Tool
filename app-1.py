# Leslio McKeown
# 09/13/2022
""" Objections: Guess the number game, the players job is to make a guess, 
and you tell them whether their guess is too high or too low. Their next guess is 
based on what you've told them. If they guess the right answer the game is done.
"""
#Sources stackoverflow 
#Helper -- Roy 
#commented and edited some flaws in my previous attemps and made the new one similar to the example given 




import constants
import copy


def sort_players():
    run = True
    teams = constants.TEAMS[::]
    players = constants.PLAYERS[::]
    num_of_teams = len(teams)
    num_of_players = len(players)
    player_per_team = num_of_players_in_team = num_of_players / num_of_teams
    teams_with_players = {}

    for team in teams:
        teams_with_players[team] = []

    team_amount = 0
    for player in players:
        if(len(teams_with_players[teams[team_amount]]) == 6):
            team_amount += 1
        curr_team = teams_with_players[teams[team_amount]]
        curr_team.append(player)

    for team in teams_with_players:
        for y, player in enumerate(teams_with_players[team]):
            teams_with_players[team][y]['height'] = int(
                teams_with_players[team][y]['height'][:2])
            if(teams_with_players[team][y]['experience'] == "NO"):
                teams_with_players[team][y]['experience'] = False
            else:
                teams_with_players[team][y]['experience'] = True

            

    print('\n')
    print("BASKETBALL TEAM STATS TOOL")
    print('\n')

    while run:
        print('---- MENU ----')
        print('\n')
        print("here are your choices: ")
        print('1.) Display stats')
        print('2.) Quit')
        print('\n')

        while run:
            try:
                user_choice = int(input('Enter an option --> '))
                if (user_choice == 1):
                    print("\n --Teams--")
                    for index, team in enumerate(teams):
                        print(str(index + 1) + ") " + str(team))
                    while run:
                        try:
                            print('\n')
                            get_team_choice = int(input('Choose a team --> '))
                            if (not(1 <= get_team_choice <= len(teams))):
                                print("Sorry but that's not a valid option")
                                break
                            print('Team: ' + teams[get_team_choice - 1] + ' Stats')
                            print('------------------------')
                            print("Number Of Players: " + 
                                str(len(teams_with_players[teams[1]])))
                            print('\n')
                            print('Players on team: ')
                            players_on_team = []
                            for player in teams_with_players[teams[get_team_choice -1]]:
                                players_on_team.append(player['name'])
                            print('\t' +', '.join (players_on_team))
                            print('\n')
                            break
                        except ValueError: 
                            print('Please only use the options that are displayed\n')
                    break 
                elif user_choice == 2:
                    print('\n')
                    print("Goodbye  ^_^ \n")
                    run = False
                else:
                    print("that's is not a valid option\n")
            except ValueError:
                print('Please only use the options that are displayed\n')


if __name__ == "__main__":
   sort_players()



