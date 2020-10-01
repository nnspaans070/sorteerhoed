
replay=1
module_1=0
module_2=0
module_3=0
module_4=0

def ask_user(): 
    global username
    username = input('Please enter your name:\n')

def vraag1():
    global module_1
    global module_2
    global module_3
    global module_4
    while True:
        vraag_antw = input('Wat is je favoriete fruit?\nA) appel\nB) peer\nC) perzik\nD) mango\n')
        if vraag_antw == 'A' or vraag_antw == 'a':
            module_1 = module_1+1
            break
        elif vraag_antw == 'B' or vraag_antw == 'b':
            module_2 = module_2+1
            break
        elif vraag_antw == 'C' or vraag_antw == 'c':
            module_3 = module_3+1
            break
        elif vraag_antw == 'D' or vraag_antw == 'd':
            module_4 = module_4 +1
            break
        else:
            print('BAKA SENPIA!!! PWEASE AWNSER WITH A, B, C OR D!')

def vraag2():
    global module_1
    global module_2
    global module_3
    global module_4
    while True:
        vraag_antw = input('Wat is je favoriete automerk?\nA) Lambo\nB) Ferrari\nC) Tesla\nD) Koenigsegg\n')
        if vraag_antw == 'A'or vraag_antw == 'a':
            module_1 = module_1+1
            break
        elif vraag_antw == 'B'or vraag_antw == 'b':
            module_2 = module_2+1
            break
        elif vraag_antw == 'C'or vraag_antw == 'c':
            module_3 = module_3+1
            break
        elif vraag_antw == 'D'or vraag_antw == 'd':
            module_4 = module_4 +1
            break
        else:
            print('BAKA SENPIA!!! PWEASE AWNSER WITH A, B, C OR D!')
            

def checker(a,b,c,d):
    global username
    dic1 = {'Software Engineering':a,'Forensisch ICT':b,'Business Data Management':c,'Interactie-technologie':d}
    awnser = max(dic1, key=dic1.get)
    print(username,'scored the best with',awnser)

def pa():
    global replay
    global module_1
    global module_2
    global module_3
    global module_4
    ua = input('want to try again?\nyes or no?\n')
    if ua == 'yes' or ua == 'Yes':
        module_1 = 0
        module_2 = 0
        module_3 = 0
        module_4 = 0
    elif ua == 'no' or ua == "No":
        replay = 0
        

while True:
    ask_user()
    vraag1()
    vraag2()
    checker(module_1,module_2,module_3,module_4)
    pa()
    if replay == 0:
        break
    else:
        pass
