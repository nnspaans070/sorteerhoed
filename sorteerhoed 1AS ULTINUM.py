# !!zorg ervoor dat de text bestand en het py bestand in dezelfde map zit
# of zorg dat je de juiste filepath schrijft(dit hoeft alleen als je niet de txt en py bestanden in hetzelfde map heb zitten!)
import os
import time
import re

replay = 1
module_1 = 0
module_2 = 0
module_3 = 0
module_4 = 0

def menu():
    print('Welcome user to the sorteerhoed 1AS ULTINUM made by team pepe')
    time.sleep(2)
    while True:
        ua2 = input('\nSelect one of the following options:\n1)Start new session\n2)view the anwsers of an user\n3)Remove the anwsers from an user\n')
        if ua2 == '1':
            break
        elif ua2 == '2':
            username4 = input('\nenter the username:\n')
            if os.path.exists(username4+'_anwsers.txt'):
                awnser_file2 = open(username4+'_anwsers.txt', 'r')
                print(awnser_file2.read())
                awnser_file2.close()
            else:
                print('User does not exist.\n\n')
        elif ua2 == '3':
            username5 = input('\n\nenter the username:\n')
            if os.path.exists(username5+'_anwsers.txt'):
                os.remove(username5+'_anwsers.txt')
                print('File succesfully removed from liberary\n\n')
                awnser_file2.close()
            else:
                print('File not found. Please enter an existing username\n\n')
    

def ask_user():
    global username
    while True:
        username = input('\nPlease enter your username:\n')
        if username.isalpha() == True:
            print('\n')
            break
        else:
            print('\nEnter a valid username\n')


def vraagfunc():
    global anwser_file
    global username
    global module_1
    global module_2
    global module_3
    global module_4
    anwser_file = open(username+'_anwsers.txt', 'w')
    vragenfile = open("vragenbestand.txt")
    for curline in vragenfile:
        if curline.startswith("--"):
            while True:
                ip = input('Senpai UwU! enter your awnser:\n')
                print('\n')
                if ip in ("A", "a"):
                    module_1 = module_1 + 1
                    anwser_file.close()
                    break
                elif ip in ("B", "b"):
                    module_2 = module_2 + 1
                    anwser_file.write('\n'+username+' anwser was: '+ip+'\n \n')
                    break
                elif ip in ("C", "c"):
                    module_3 = module_3 + 1
                    anwser_file.write('\n'+username+' anwser was: '+ip+'\n \n')
                    break
                elif ip in ("D", "d"):
                    module_4 = module_4 + 1
                    anwser_file.write('\n'+username+' anwser was: '+ip+'\n \n')
                    break
                else:
                    print('BAKA SENPIA!!! PWEASE AWNSER WITH A, B, C OR D!')
        elif curline.startswith("E.N.D."):
            break
        else:
            anwser_file.write(curline)
            print(curline)
            
    vragenfile.close()
    #anwser_file.close()

def checker(a, b, c, d):
    global username
    global anwser_file
    dic1 = {'Software Engineering': a, 'Forensisch ICT': b, 'Business Data Management': c, 'Interactie-technologie': d}
    anwser = max(dic1, key=dic1.get)
    anwser_file.write(username+' scored the best with:\n'+anwser+'\n')
    print(username,'scored the best with:\n', anwser+'\n')
    anwser_file.close()

def pa():
    global replay
    global module_1
    global module_2
    global module_3
    global module_4
    while True:
        ua = input('Select one of the following options:\n1)Start new session\n2)view the anwsers of an user\n3)Remove the awnsers of an user\n4)close application\n')
        if ua == '1':#begin opnieuw
            module_1 = 0
            module_2 = 0
            module_3 = 0
            module_4 = 0
            break
        elif ua == '4':#close app
            replay = 0
            break
        elif ua == '2':#view file
            username2 = input('\n\nEnter an username:\n')
            if os.path.exists(username2+'_anwsers.txt'):
                awnser_file2 = open(username2+'_anwsers.txt', 'r')
                print(awnser_file2.read())
                awnser_file2.close()
            else:
                print('User does not exist.\n\n')
        elif ua == '3':#remove file
            username3 = input('\n\nenter the username:\n')
            if os.path.exists(username3+'_anwsers.txt'):
                os.remove(username3+'_anwsers.txt')
                print('File succesfully removed from liberary\n\n')
                awnser_file2.close()
            else:
                print('File not found. Please enter an existing username\n\n')
        else:
            print('\n\nSenpaiiiii! Pwease anwser with a number!\n\n')


menu()
while True:
    ask_user()
    vraagfunc()
    checker(module_1, module_2, module_3, module_4)
    pa()
    if replay == 0:
        break
    else:
        pass
