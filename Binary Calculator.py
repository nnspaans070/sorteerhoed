def bincalc():
    #binary calculator
    i_1 = input('Enter the first binary number! ')
    i_2 = input('Enter the second binary number! ')
    i_1 = int('0b'+i_1, 2)
    i_2 = int('0b'+i_2, 2)
    entry = input('enter either + ,- , * or / ! ')
    if entry == '+':
        print(i_1+i_2)
        print(bin(i_1+i_2))
    elif entry == '-':
        print(i_1-i_2)
        print(bin(i_1-i_2))
    elif entry == '*':
        print(i_1*i_2)
        print(bin(i_1*i_2))
    elif entry == '/':
        x=int(i_1/i_2)
        print(x)
        print(bin(x))
    else:
        print('ERROR\n\n')    

def deccalc():
    x = int(input('Enter a decimal number! '))
    print(bin(x))


def menu():
    while True:
        a = input('1) Binary to decimal\n2) Binary calculator\n3) Close program\n')
        if a == '1':
            deccalc()
        elif a == '2':
            bincalc()
        else:
            break

menu()
