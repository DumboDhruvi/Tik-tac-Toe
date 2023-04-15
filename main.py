A = {'row1': [' ', ' ', ' '], 'row2': [' ', ' ', ' '], 'row3': [' ', ' ', ' ']}
def main(): # dict A is used to store the game data as it proceeds
    A = {'row1': [' ', ' ', ' '], 'row2': [' ', ' ', ' '], 'row3': [' ', ' ', ' ']}
    i = 0 # i determines the move turn when it is even it is x"s turn and vice veesa
    while True: # loop for taking mutiple inputs until game is won or unwinable or users ends it with ctrl c
        pick, coordinate = intech(i) #intech function handles the user input
        row_num, ordinate = coordinate.split(' ') # converts raw input to readable form
        A = game_rule(A, pick, row_num, ordinate)
        for key in A:
            print(key, A[key])
        if victory(A):
            print('game over')
            break
        i += 1

def intech(i):
    if i % 2 == 0:
        pick = 'X'
        coordinate = input('for X row(1,2,3), 1, 2, 3: ')
    else:
        pick = 'O'
        coordinate = input('for O row(1,2,3), 1, 2, 3: ')
    return pick, coordinate




def game_rule(A, pick, row_num, ordinate):
    pick = pick.capitalize()
    key = 'row' + str(row_num)
    A[key].insert(int(ordinate), str(pick))
    A[key].remove(str(' '))
    return A


def victory(A):
    for i in range(1, 4):
        key = 'row' + str(i)
        if A[key][0] == A[key][1] == A[key][2] == 'X':
            return True, 'X won'
        else:
            pass
        if A[key][0] == A[key][1] == A[key][2] == 'O':
            return True, 'O won'
        else:
            pass
    for i in range(3):
        if A['row1'][i] == A['row2'][i] == A['row3'][i] == 'X':
            return True, 'X won'
        if A['row1'][i] == A['row2'][i] == A['row3'][i] == 'O':
            return True, 'O won'
    if A['row1'][0] == A['row2'][1] == A['row3'][2] == 'X':
        return True, 'X Won'
    elif A['row1'][0] == A['row2'][1] == A['row3'][2] == 'O':
        return True, 'O Won'
    if A['row1'][2] == A['row2'][1] == A['row3'][0] == 'X':
        return True, 'X Won'
    if A['row1'][2] == A['row2'][1] == A['row3'][0] == 'O':
        return True, 'O Won'

    else:
        return False




if __name__ == '__main__':
    main()
    
