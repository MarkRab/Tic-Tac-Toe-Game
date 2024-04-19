
# WELCOME INTRO
def intro():
    print('---------Welcome to Tic Tac Toe!-----------')
    
    introlist = {'line1':'   |   |   ',
            'line2':' 3 | 6 | 9 ',
            'line3':'   |   |   ',
            'line4':'-----------',
            'line5':'   |   |   ',
            'line6':' 2 | 5 | 8 ',
            'line7':'   |   |   ',
            'line8':'-----------',
            'line9':'   |   |   ',
           'line10':' 1 | 4 | 7 ',
           'line11':'   |   |   '}

    for key,value in introlist.items():
        print(value)
    print('Please remember the locations of values')


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
        ready_to_play = input('Are you ready to play? Enter Yes or No. ')

        if ready_to_play not in ['Yes','No']:
            print('Sorry, you need to input Yes or No')
        elif ready_to_play == 'Yes':
            return True
        else:
            return False



# tic game start
def next_pos():
    
    next_position = 'wrong'
    next_position = input('Choose your next position: (1-9)')
    
    while next_position.isdigit() != True: 
        print('Please input a number')
        next_position = input('Choose your next position: (1-9)')

    while next_position not in ['1','2','3','4','5','6','7','8','9']:
        print('Please input a number in the range(1-9)')
        next_position = input('Choose your next position: (1-9)')

    return next_position

def judge_win(gamelist):
    a1 = gamelist[9][1]
    a2 = gamelist[5][1]
    a3 = gamelist[1][1]
    a4 = gamelist[9][5]
    a5 = gamelist[5][5]
    a6 = gamelist[1][5]
    a7 = gamelist[9][1]
    a8 = gamelist[9][5]
    a9 = gamelist[9][9]

    judge = a1==a2==a3!=' ' or a4==a5==a6!=' ' or a7==a8==a9!=' ' or a1==a4==a7!=' ' or a2==a5==a8!=' ' or a3==a6==a9!=' ' or a1==a5==a9!=' ' or a3==a5==a7!=' '
    return judge

def update_list(inistart):

    one=' '
    two=' '
    three=' '
    four=' '
    five=' '
    six=' '
    seven=' '
    eight=' '
    nine=' '

    gamelist = ['   |   |   ',
            ' {} | {} | {} '.format(three,six,nine),
            '   |   |   ',
            '-----------',
            '   |   |   ',
            ' {} | {} | {} '.format(two,five,eight),
            '   |   |   ',
            '-----------',
            '   |   |   ',
            ' {} | {} | {} '.format(one,four,seven),
           '   |   |   ']

    compare_list={'1':one,'2':two,'3':three,'4':four,'5':five,'6':six,'7':seven,'8':eight,'9':nine
    }

    # DEFINE 2 LISTS FOR INPUT X O
    list1=['X','O','X','O','X','O','X','O','X']
    list2=['O','X','O','X','O','X','O','X','O']
    finallist=[]

    if inistart=='X':
        finallist= list1

    elif inistart=='O':
        finallist= list2

    # keep on while not win
    i=0
    lastpos=''
    result='Wrong'

    while result != True:
        nextpos = next_pos()
        if nextpos == lastpos:
            print('You need to choose different position')
            continue
        if nextpos == '1':
            one = finallist[i]
            gamelist[9] = ' {} | {} | {} '.format(one, four, seven)
        elif nextpos == '2':
            two = finallist[i]
            gamelist[5] = ' {} | {} | {} '.format(two, five, eight)
        elif nextpos == '3':
            three = finallist[i]
            gamelist[1] = ' {} | {} | {} '.format(three, six, nine)
        elif nextpos == '4':
            four = finallist[i]
            gamelist[9] = ' {} | {} | {} '.format(one, four, seven)
        elif nextpos == '5':
            five = finallist[i]
            gamelist[5] = ' {} | {} | {} '.format(two, five, eight)
        elif nextpos == '6':
            six = finallist[i]
            gamelist[1] = ' {} | {} | {} '.format(three, six, nine)
        elif nextpos == '7':
            seven = finallist[i]
            gamelist[9] = ' {} | {} | {} '.format(one, four, seven)
        elif nextpos == '8':
            eight = finallist[i]
            gamelist[5] = ' {} | {} | {} '.format(two, five, eight)
        elif nextpos == '9':
            nine = finallist[i]
            gamelist[1] = ' {} | {} | {} '.format(three, six, nine)

        for each in gamelist:
            print(each)
        result = judge_win(gamelist)
        i+=1
        lastpos = nextpos

    if result == True:
        print('Congratulations! You won.')

        playagain='Wrong'
        while playagain not in ['Yes','No']:
            playagain = input('Do you want to play again? Yes or No')

        if playagain == 'Yes':
            one=' '
            two=' '
            three=' '
            four=' '
            five=' '
            six=' '
            seven=' '
            eight=' '
            nine=' '

            main()
        elif playagain == 'No':
            print('GG. Have a good day')

def main():

    intro()
    inistart = ini_start()
    ready = ready_play()

    if ready == True:
        pass
    if ready == False:
        return

 #   next_pos()
        
    update_list(inistart)
