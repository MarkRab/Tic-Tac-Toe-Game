# WELCOME INTRO
def Intro():
    print('Welcome to Tic Tac Toe!')


# CHOOSE X OR O
def ini_start():
    initial_start = 'wrong'

    while initial_start not in ['X','O']:
        initial_start = input('Player 1: Do you want to be X or O? ')

        if initial_start not in ['X','O']:
            print('Sorry, please input X or O')
        
    return initial_start

# ready to play?
def ready_play():
    ready_to_play = 'wrong'

    while ready_to_play not in ['Yes','No']:
        initial_start = input('Are you ready to play? Enter Yes or No. ')

        if ready_to_play not in ['Yes','No']:
            print('Sorry, please input X or O')
        elif ready_to_play == 'Yes':
            return True
        else:
            return False

gamelist = {'line1':'   |   |   ',
            'line2':'   |   |   ',
            'line3':'   |   |   ',
            'line4':'-----------',
            'line5':'   |   |   ',
            'line6':'   |   |   ',
            'line7':'   |   |   ',
            'line8':'-----------',
            'line9':'   |   |   ',
           'line10':'   |   |   ',
           'line11':'   |   |   '}

# tic game start
def next_pos():
    
    next_position = 'wrong'
    
    while next_position.isdigit() == False or next_position not in range(1,10):
        next_position = input('Choose your next position: (1-9)')
        print(gamelist)

        if next_position not in range(1,10):
            print('Please input integar from 1 to 9')
    
    real_next_position = int(next_position)
    return real_next_position

def update_gamelist():
    # DEFINE 2 LISTS FOR INPUT X O
    list1=['X','O','X','O','X','O','X','O','X']
    list2=['O','X','O','X','O','X','O','X','O']
    finallist=[]

    if ini_start()=='X':
        finallist= list1

    elif ini_start()=='O':
        finallist= list2

        
    # keep on while not True
        while 