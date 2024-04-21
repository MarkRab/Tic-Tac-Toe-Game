
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

    while initial_start not in ['X','x','O','o']:
        initial_start = input('Player 1: Do you want to be X or O? ')

        if initial_start not in ['X','x','O','o']:
            print('Sorry, please input X or O')
    
    if initial_start in ['X','x']:
        print('Player 2 will have O')
    elif initial_start in ['O','o']:
        print('Player 2 will have X')
        
    return initial_start

# READY TO PLAY? YES OR NO
def ready_play():
    ready_to_play = 'wrong'

    while ready_to_play.lower() not in ['yes','no']:
        ready_to_play = input('Are you ready to play? Enter Yes or No. ')

        if ready_to_play.lower() not in ['yes','no']:
            print('Sorry, you need to input Yes or No')
        elif ready_to_play.lower() == 'yes':
            return True
        else:
            return False

# CHOOSE NEXT POSITION
def next_pos():
    
    next_position = 'wrong'
    next_position = input('Choose your position: (1-9)')
    
    while next_position.isdigit() != True: 
        print('Please input a number')
        next_position = input('Choose your position: (1-9)')

    while next_position not in ['1','2','3','4','5','6','7','8','9']:
        print('Please input a number in the range(1-9)')
        next_position = input('Choose your position: (1-9)')

    return next_position

# JUDGE WHETHER WIN OR NOT. STRAIGHT AND DIAGONAL LINES
def judge_win(gamelist):
    a1 = gamelist[9][1]
    a2 = gamelist[5][1]
    a3 = gamelist[1][1]
    a4 = gamelist[9][5]
    a5 = gamelist[5][5]
    a6 = gamelist[1][5]
    a7 = gamelist[9][9]
    a8 = gamelist[5][9]
    a9 = gamelist[1][9]

    return a1==a2==a3!=' ' or a4==a5==a6!=' ' or a7==a8==a9!=' ' or a1==a4==a7!=' ' or a2==a5==a8!=' ' or a3==a6==a9!=' ' or a1==a5==a9!=' ' or a3==a5==a7!=' '

# UPDATE GAMELIST AND REFER JUDGE FUNCTION TO JUDGE
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

    # DEFINE 2 LISTS FOR INPUT X O
    list1=['X','O','X','O','X','O','X','O','X']
    list2=['O','X','O','X','O','X','O','X','O']
    finallist=[]

    if inistart=='X' or 'x':
        finallist= list1

    elif inistart=='O' or 'o':
        finallist= list2

    # keep on while not win
    i=0
    lastpos=''
    result=False

    while result == False:
        if i%2 ==0:
            print("-------------------------\n \nPlayer 1's turn")
        else:
            print("-------------------------\n \nPlayer 2's turn")

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
        if one!=' ' and two!=' ' and three!=' '  and four!=' ' and five!=' ' and six!=' ' and seven!=' ' and eight!=' ' and nine!=' ' and result!=True:
            print('All blanks taken, tie! GG, have a good day.')
            play_again()

    if result == True:
        if i%2==0:
            print('Congratulations! Player 2 won!!')
        else:
            print('Congratulations! Player 1 won!!')
        play_again()

def play_again():
    playagain='Wrong'
    while playagain not in ['Yes','No']:
        playagain = input('Do you want to play again? Yes or No: ')

    if playagain == 'Yes':

        main()
    elif playagain == 'No':
        print('GG. Have a good day')

# MAIN TO CONNECT ALL FUNCTION TOGETHER
def main():

    intro()
    inistart = ini_start()
    ready = ready_play()

    if ready == True:
        pass
    if ready == False:
        return

    update_list(inistart)

main()