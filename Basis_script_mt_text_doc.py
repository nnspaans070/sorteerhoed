# !!zorg ervoor dat de text bestand en het py bestand in dezelfde map zit
# of zorg dat je de juiste filepath schrijft(dit hoeft alleen als je niet de txt en py bestanden in hetzelfde map heb zitten!) 

replay = 1
module_1 = 0
module_2 = 0
module_3 = 0
module_4 = 0


def ask_user():
    global username
    username = input('Please enter your name:\n')


def vraagfunc():
    vragenfile = open("vragenbestand.txt")
    global module_1
    global module_2
    global module_3
    global module_4
    for curline in vragenfile:
        if curline.startswith("--"):
            while True:
                ip = input('Senpai UwU! enter your awnser:\n')
                print('\n')
                if ip == 'A' or ip == 'a':
                    module_1 = module_1 + 1
                    break
                elif ip == 'B' or ip == 'b':
                    module_2 = module_2 + 1
                    break
                elif ip == 'C' or ip == 'c':
                    module_3 = module_3 + 1
                    break
                elif ip == 'D' or ip == 'd':
                    module_4 = module_4 + 1
                    break
                else:
                    print('BAKA SENPIA!!! PWEASE AWNSER WITH A, B, C OR D!')
        elif curline.startswith("E.N.D."):
            break
        else:
            print(curline)
    vragenfile.close()


def checker(a, b, c, d):
    global username
    dic1 = {'Software Engineering': a, 'Forensisch ICT': b, 'Business Data Management': c, 'Interactie-technologie': d}
    awnser = max(dic1, key=dic1.get)
    print(username, 'scored the best with', awnser)


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
    vraagfunc()
    checker(module_1, module_2, module_3, module_4)
    pa()
    if replay == 0:
        break
    else:
        pass
