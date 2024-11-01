#TicTacToe


import random
#create dictionary to hold space info for the board
grid_Board = {'A1': [' '],'A2': [' '],'A3': [' '],'B1': [' '],'B2': [' '],'B3': [' '],'C1': [' '],'C2': [' '],'C3': [' ']}
#create grid for game
def create_grid():
    translation = {39: None}
    grid_A = 'A'
    grid_B = 'B'
    grid_C = 'C'
    grid_1 = ' 1 '
    grid_2 = ' 2 '
    grid_3 = ' 3 '
    grid_A1 = grid_Board['A1']
    grid_A2 = grid_Board['A2']
    grid_A3 = grid_Board['A3']
    grid_B1 = grid_Board['B1']
    grid_B2 = grid_Board['B2']
    grid_B3 = grid_Board['B3']
    grid_C1 = grid_Board['C1']
    grid_C2 = grid_Board['C2']
    grid_C3 = grid_Board['C3']
    print('  ' + grid_1 + ' ' + grid_2 + ' ' + grid_3)
    print(grid_A + ' ' + str(grid_A1).translate(translation) + ' ' + str(grid_A2).translate(translation) + ' ' + str(grid_A3).translate(translation))
    print(grid_B + ' ' + str(grid_B1).translate(translation) + ' ' + str(grid_B2).translate(translation) + ' ' + str(grid_B3).translate(translation))
    print(grid_C + ' ' + str(grid_C1).translate(translation) + ' ' + str(grid_C2).translate(translation) + ' ' + str(grid_C3).translate(translation))

#Create holding list for X and O choices
choice_list = ['X','O']
#List to hold r key for rolling
roll_list = ['r']

class Player:

    def __init__(self):
        #Ask each player for their name
        player1 = input('Input name for player 1.\n')
        player2 = input('Input name for player 2.\n')
        print('')
        self.player1 = player1
        self.player2 = player2

    def player_order(self,player1,player2):

        print('Whoever rolls the highest gets to play first and pick X or O')

        roll1 = input(player1 + ' enter r to roll: ')
        while roll1 not in roll_list:
            roll1 = input(player1 + ' enter r to roll: ')

        if roll1 == 'r':
            player1_roll = random.randint(1,6)
            print(player1 + ' got a ' + str(player1_roll))

        roll2 = input(player2 + ' enter r to roll: ')
        while roll2 not in roll_list:
            roll2 = input(player2 + ' enter r to roll: ')

        if roll2 == 'r':
            player2_roll = random.randint(1,6)
            print(player2 + ' got a ' + str(player2_roll))
        
        def reroll():
            print('')
            print('Both players rolled the same number so roll again!')
            roll1 = input(player1 + ' enter r to roll: ')
            while roll1 not in roll_list:
                roll1 = input(player1 + ' enter r to roll: ')

            if roll1 == 'r':
                player1_roll = random.randint(1,6)
                print(player1 + ' got a ' + str(player1_roll))

            roll2 = input(player2 + ' enter r to roll: ')

            if roll2 == 'r':
                player2_roll = random.randint(1,6)
                print(player2 + ' got a ' + str(player2_roll))
            rolls = [player1_roll, player2_roll]
            return rolls

        while player1_roll == player2_roll:
                rolls = reroll()
                player1_roll = rolls[0]
                player2_roll = rolls[1]
        

        print('')


        def roll_win(player1_roll,player2_roll):
                if player1_roll > player2_roll:
                    print(player1 + ' is going first')
                    self.player_Order = [player1,player2]
                    choice = input("Do you want X or O(In caps please): ")
                    while choice not in choice_list:
                        choice = input("Do you want X or O(In caps please): ")
                    if choice == 'X':
                        self.crosses = 1
                        self.noughts = 2
                    elif choice == 'O':
                        self.crosses = 2
                        self.noughts = 1
                    else:
                        print('error in code')
                elif player1_roll < player2_roll:
                    self.player_Order = [player2,player1]
                    print(player2 + ' is going first')
                    choice = input("Do you want X or O(In caps please): ")
                    while choice not in choice_list:
                        choice = input("Do you want X or O(In caps please): ")
                    if choice == 'X':
                        self.crosses = 1
                        self.noughts = 2
                    elif choice == 'O':
                        self.crosses = 2
                        self.noughts = 1
                    else:
                        print('error in code')
                else:
                    print('error in code')

        roll_win(player1_roll,player2_roll)
    
def win_check(grid_Board):
    winning_combinations = [['A1', 'A2', 'A3'],['B1', 'B2', 'B3'],['C1', 'C2', 'C3'],['A1', 'B1', 'C1'],['A2', 'B2', 'C2'],['A3', 'B3', 'C3'],['A1', 'B2', 'C3'],['A3', 'B2', 'C1']]
    
    win = False

    for combo in winning_combinations:
        
        #print(grid_Board[combo[0]] + grid_Board[combo[1]] + grid_Board[combo[2]])
        if grid_Board[combo[0]] == grid_Board[combo[1]] == grid_Board[combo[2]]:
            if grid_Board[combo[0]] != [' '] and grid_Board[combo[1]] != [' '] and grid_Board[combo[2]] != [' ']:
                #print('true')
                win = True
    return win




def play_XorO(XandO):
    filled_spaces = []
    current = player_order[0]
    #print(current)
    while win_check(grid_Board) ==  False:
        print(current + '\'s Turn')
        choice = input('Where would you like to pick on the board:\n')
        #print(choice)
        Choice = choice.upper()
        while Choice not in grid_Board.keys():
            choice = input('Where would you like to pick on the board:\n')
            Choice = choice.upper()
        #print(Choice)
        while Choice in filled_spaces:
            choice = input('That space is already filled, where would you like to pick on the board:\n')
            Choice = choice.upper()
            while Choice not in grid_Board.keys():
                choice = input('Where would you like to pick on the board:\n')
                Choice = choice.upper()
        filled_spaces.append(Choice)
        #print(filled_spaces)
        grid_Board[Choice] = XandO[current]
        print('')
        create_grid()
        if current == player_order[0]:
            current = player_order[1]
        else:
            current = player_order[0]
        print('')
        #Check for tie
        #print(grid_Board.values())
        if [' '] not in grid_Board.values() and win_check(grid_Board) ==  False:
            tie = True
        else:
            tie = False
        if tie == True:
            if current == player_order[0]:
                current = player_order[1]
            else:
                current = player_order[0]
            return ('It\'s a tie try again!')

    if current == player_order[0]:
        current = player_order[1]
    else:
        current = player_order[0]
    return ('The winner is ' + current + '!')
        
        
    



    



#Call function player_order from class player
player = Player()
player1 = player.player1
player2 = player.player2
player.player_order(player1,player2)
player_order = player.player_Order
if player.crosses == 1:
    first = 'X'
    second = 'O'
elif player.noughts == 1:
    first = 'O'
    second = 'X'
#print(player_order)
XandO = {player_order[0]: [first], player_order[1]: [second]}
print('')
create_grid()
#print(XandO)
print(play_XorO(XandO))


