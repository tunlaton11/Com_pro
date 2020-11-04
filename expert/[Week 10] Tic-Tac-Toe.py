"""[Week 10] Tic-Tac-Toe"""
def exce(table):
    """sss"""
    for i in table:
        print(i, end='')

def main():
    """[Week 10] Tic-Tac-Toe"""
    check = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    table = ['+-+-+-+', '\n', '|', 1, '|', 2, '|', 3, '|', '\n',
             '+-+-+-+', '\n', '|', 4, '|', 5, '|', 6, '|', '\n',
             '+-+-+-+', '\n', '|', 7, '|', 8, '|', 9, '|', '\n', '+-+-+-+', '\n', '\n']
    win1 = {1, 2, 3}
    win2 = {4, 5, 6}
    win3 = {7, 8, 9}
    win4 = {1, 4, 7}
    win5 = {2, 5, 8}
    win6 = {3, 6, 9}
    win7 = {1, 5, 9}
    win8 = {3, 5, 7}
    turn_x = set()
    turn_o = set()
    count = 1
    print("Welcome to OX!\n")
    exce(table)
    while True:
        if count == 10:
            print("Draw!!")
            break
        elif count % 2 != 0:
            count += 1
            print('It\'s X\'s turn!')
            while True:
                val = input("Please enter cell number (1-9) --> ")
                if val in check:
                    break
            check.remove(val)
            val = int(val)
            turn_x.add(val)
            table[table.index(val)] = 'X'
            exce(table)
            if turn_x.intersection(win1) == win1 or turn_x.intersection(win2) == win2 or\
                turn_x.intersection(win3) == win3 or turn_x.intersection(win4) == win4 or\
                turn_x.intersection(win5) == win5 or turn_x.intersection(win6) == win6 or\
                turn_x.intersection(win7) == win7 or turn_x.intersection(win8) == win8:
                print('The winner is X!!')
                break
        else:
            count += 1
            print('It\'s O\'s turn!')
            while True:
                val = input("Please enter cell number (1-9) --> ")
                if val in check:
                    break
            check.remove(val)
            val = int(val)
            turn_o.add(val)
            table[table.index(val)] = 'O'
            exce(table)
            if turn_o.intersection(win1) == win1 or turn_o.intersection(win2) == win2 or\
                turn_o.intersection(win3) == win3 or turn_o.intersection(win4) == win4 or\
                turn_o.intersection(win5) == win5 or turn_o.intersection(win6) == win6 or\
                turn_o.intersection(win7) == win7 or turn_o.intersection(win8) == win8:
                print('The winner is O!!')
                break

main()
