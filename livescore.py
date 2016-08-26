from data.manager import Controller

controller = Controller()

def print_main_menu():
    print('MAIN MENU : \n')
    print('1. Press 1 to see all matches.')
    print('2. Press 2 to see all favourite matches.')
    print('3. Press 3 to see match details.')
    print('4. Press 4 to add match to favourites.')
    print('5. Press 5 to remove match from favourites.')
    print('6. Press 6 to see league table.')
    print('7. Press \'e\' for EXIT.')


def print_all_matches():
    print('\n')
    controller.printAllMatches()
    print('\n')


def print_all_favourite_matches():
    print('\n')
    controller.printAllFavouriteMatches()
    print('\n')


def add_to_favourites():
    match = ''
    while match != 'e':
        print('Enter the ID of the match or \'e\' for exit : ')
        match = input("-> ")
        if match == 'e':
            return
        try:
            match = (int)(match)
        except Exception as e:
            print('Wrong input! Try again.')
            continue
        controller.addToFavourites(match)


def remove_from_favourites():
    match = ''
    while match != 'e':
        print('Enter the ID of the match or \'e\' for exit : ')
        match = input("-> ")
        if match == 'e':
            return
        try:
            match = (int)(match)
        except Exception as e:
            print('Wrong input! Try again.')
            continue
        controller.removeFromFavourites(match)


def league_tables_menu():
    print('\n')
    controller.printAllLeagues()
    print('\n')
    league = ''
    while league != 'e':
        print('Enter the ID of the league or \'e\' for exit : ')
        league = input("-> ")
        if league == 'e':
            return
        try:
            league = (int)(league)
        except Exception as e:
            print('Wrong input! Try again.')
            continue
        controller.printLeagueTable(league)
        print('\n')
        team_details_menu()


def match_details_menu():
    match = ''
    while match != 'e':
        print('Enter the ID of the match or \'e\' for exit : ')
        match = input("-> ")
        if match == 'e':
            return
        try:
            match = (int)(match)
        except Exception as e:
            print('Wrong input! Try again.')
            continue
        controller.printMatchDetails(match)


def team_details_menu():
    team = ''
    while team != 'e':
        print('If you want information about team : \n' +\
              'Enter the ID of the team or \'e\' for exit : ')
        team = input("-> ")
        if team == 'e':
            return
        try:
            team = (int)(team)
        except Exception as e:
            print('Wrong input! Try again.')
            continue
        controller.printTeamDetails(team)


def livescore():
    choise = ''
    while choise != 'e':
        print_main_menu()    
        choise = input('-> ')
        if choise == '1':
            print_all_matches()
        elif choise == '2':
            print_all_favourite_matches()
        elif choise == '3':
            match_details_menu()
        elif choise == '4':
            add_to_favourites()
        elif choise == '5':
            remove_from_favourites()
        elif choise == '6':
            league_tables_menu()
        elif choise == 'e':
            return
        else:
            print('Wrong input! Try again.')

if __name__ == '__main__':
    livescore()
