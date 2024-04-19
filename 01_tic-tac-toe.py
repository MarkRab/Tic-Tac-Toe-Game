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

reset_gamelist = {'line1':'   |   |   ',
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

def judge_win(gamelist):
    a1 = gamelist['line10'][1]
    a2 = gamelist['line6'][1]
    a3 = gamelist['line1'][1]
    a4 = gamelist['line10'][5]
    a5 = gamelist['line6'][5]
    a6 = gamelist['line1'][5]
    a7 = gamelist['line10'][9]
    a8 = gamelist['line6'][9]
    a9 = gamelist['line1'][9]

    return a1==a2==a3 or a4==a5==a6 or a7==a8==a9 or a1==a4==a7 or a2==a5==a8 or a3==a6==a9 or a1==a5==a9 or a3==a5==a7


def update_list():

    # DEFINE 2 LISTS FOR INPUT X O
    list1=['X','O','X','O','X','O','X','O','X']
    list2=['O','X','O','X','O','X','O','X','O']
    finallist=[]

    if ini_start()=='X':
        finallist= list1

    elif ini_start()=='O':
        finallist= list2

    index_position={
    '1':gamelist['line10'][1],
    '2':gamelist['line6'][1],
    '3':gamelist['line1'][1],
    '4':gamelist['line10'][5],
    '5':gamelist['line6'][5],
    '6':gamelist['line1'][5],
    '7':gamelist['line10'][9],
    '8':gamelist['line6'][9],
    '9':gamelist['line1'][9],
    }

    # keep on while not win
    i=0
    result='Wrong'

    while result == False:
        next_pos()
        index_position[next_pos]=finallist[i]
        print(gamelist)
        result = judge_win(gamelist)
        i+=1

    if result == True:
        print('Correct')

        playagain='Wrong'
        while playagain not in ['Yes','No']:
            playagain = input('Do you want to play again? Yes or No')

        if playagain == 'Yes':
            gamelist = reset_gamelist
            main()
        elif playagain == 'No':
            print('GG. Have a good day')

def main():
    ini_start()
    ready_play()
    update_list()