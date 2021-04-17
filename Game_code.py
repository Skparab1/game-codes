
from random import randint
'''from random import randint
Random_num = randint(1,100)
num_tries = 0
Guess = int(input ('Welcome to secret number. press 1 followed by enter to continue '))
while Guess != Random_num:
    Guess = int(input ('enter a guess '))
    if Guess > Random_num:
        print('too high ')
    elif Guess < Random_num:
        print('too low ')
    else :
        print ('that is correct')
    num_tries = num_tries + 1
  
print ('good job. you took ' , num_tries , 'tries')
Random_num = randint(1,100)

import time
j = 1
h = 10
while j < 10:
    i = 1
    while i < 50:
        print(' ')
        i += 1
    print ('XXXXXyyyZZZyyYXZYZBX ABCDEFGHIJKklnmentolQRSTUVWXY  bunny bunny BUnny BUNNY BUNNY BUNNY BUNNY')
    l = 0
    while l < h:
        print(' ')
        l += 1
    time.sleep (0.15)
    j += 1
    h -= 1
    
print ('Shubham programming presents')
time.sleep (0.5)
print ('------------------------------------------------------------------------------------')
print ('Paving the road of numbers')
print ('------------------------------------------------------------------------------------')
input ('press enter to continue')
print ('------------------------------------------------------------------------------------')
print ('warping numbers')
print ('------------------------------------------------------------------------------------')
m = -30
while m < 20:
    print(m , '     ' , m - 1 , '     ' , m - 2 , '     ' , m - 3 , '     ' , m - 4 , '     ' , m - 5 , '     ' , m - 6)
    time.sleep (0.15)
    m += 1
print ('------------------------------------------------------------------------------------')
print ('Scroll up for a re-experience')
print ('------------------------------------------------------------------------------------')


input ('press enter to continue')
m = -30
random_num = 0
num1 = num2 = num3 = num4 = num5 = num6 = num7 = num8 = num9 = num10 = num11 = num12 = num13 = num14 = 0
while m < 100:
    random_num = randint(0, 15)
    if random_num == 1 :
        print('|WWWWWW|      |      |      |      |      |      |      |      |      |      |      |      |      |' )
        num1 = num1 + 1
    elif random_num == 2 :
        num2 = num2 + 1
        print('|      |WWWWWW|      |      |      |      |      |      |      |      |      |      |      |      |' )
    elif random_num == 3 :
        num3 = num3 + 1
        print('|      |      |WWWWWW|      |      |      |      |      |      |      |      |      |      |      |' )
    elif random_num == 4 :
        num4 = num4 + 1
        print('|      |      |      |WWWWWW|      |      |      |      |      |      |      |      |      |      |' )
    elif random_num == 5 :
        num5 = num5 + 1
        print('|      |      |      |      |WWWWWW|      |      |      |      |      |      |      |      |      |' )
    elif random_num == 6 :
        num6 = num6 + 1
        print('|      |      |      |      |      |WWWWWW|      |      |      |      |      |      |      |      |' )
    elif random_num == 7 :
        num7 = num7 + 1
        print('|      |      |      |      |      |      |WWWWWW|      |      |      |      |      |      |      |' )
    elif random_num == 8 :
        num8 = num8 + 1
        print('|      |      |      |      |      |      |      |WWWWWW|      |      |      |      |      |      |' )
    elif random_num == 9 :
        num9 = num9 + 1
        print('|      |      |      |      |      |      |      |      |WWWWWW|      |      |      |      |      |' )
    elif random_num == 10 :
        num10 = num10 + 1
        print('|      |      |      |      |      |      |      |      |      |WWWWWW|      |      |      |      |' )
    elif random_num == 11 :
        num11 = num11 + 1
        print('|      |      |      |      |      |      |      |      |      |      |WWWWWW|      |      |      |' )
    elif random_num == 12 :
        num12 = num12 + 1
        print('|      |      |      |      |      |      |      |      |      |      |      |WWWWWW|      |      |' )
    elif random_num == 13 :
        num13 = num13 + 1
        print('|      |      |      |      |      |      |      |      |      |      |      |      |WWWWWW|      |' )
    elif random_num == 14 :
        num14 = num14
        print('|      |      |      |      |      |      |      |      |      |      |      |      |      |WWWWWW|' )
    
    time.sleep (0.15)
    m += 1
'''
import time
def generate_random_obstacle():
    m = -30
    random_num = 0
    random_num = randint(0, 15)
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    num6 = 0
    num7 = 0
    num8 = 0
    num9 = 0
    num10 = 0
    num11 = 0
    num12 = 0
    num13 = 0
    num14 = 0
    if random_num == 1 :
        print('|WWWWWW|      |      |      |      |      |      |      |      |      |      |      |      |      |' )
        num1 = num1 + 1
    elif random_num == 2 :
        num2 = num2 + 1
        print('|      |WWWWWW|      |      |      |      |      |      |      |      |      |      |      |      |' )
    elif random_num == 3 :
        num3 = num3 + 1
        print('|      |      |WWWWWW|      |      |      |      |      |      |      |      |      |      |      |' )
    elif random_num == 4 :
        num4 = num4 + 1
        print('|      |      |      |WWWWWW|      |      |      |      |      |      |      |      |      |      |' )
    elif random_num == 5 :
        num5 = num5 + 1
        print('|      |      |      |      |WWWWWW|      |      |      |      |      |      |      |      |      |' )
    elif random_num == 6 :
        num6 = num6 + 1
        print('|      |      |      |      |      |WWWWWW|      |      |      |      |      |      |      |      |' )
    elif random_num == 7 :
        num7 = num7 + 1
        print('|      |      |      |      |      |      |WWWWWW|      |      |      |      |      |      |      |' )
    elif random_num == 8 :
        num8 = num8 + 1
        print('|      |      |      |      |      |      |      |WWWWWW|      |      |      |      |      |      |' )
    elif random_num == 9 :
        num9 = num9 + 1
        print('|      |      |      |      |      |      |      |      |WWWWWW|      |      |      |      |      |' )
    elif random_num == 10 :
        num10 = num10 + 1
        print('|      |      |      |      |      |      |      |      |      |WWWWWW|      |      |      |      |' )
    elif random_num == 11 :
        num11 = num11 + 1
        print('|      |      |      |      |      |      |      |      |      |      |WWWWWW|      |      |      |' )
    elif random_num == 12 :
        num12 = num12 + 1
        print('|      |      |      |      |      |      |      |      |      |      |      |WWWWWW|      |      |' )
    elif random_num == 13 :
        num13 = num13 + 1
        print('|      |      |      |      |      |      |      |      |      |      |      |      |WWWWWW|      |' )
    elif random_num == 14 :
        num14 = num14
        print('|      |      |      |      |      |      |      |      |      |      |      |      |      |WWWWWW|' )
    
        time.sleep (0.15)
        m += 1
print('\n' * 50)
print(10 * '--------')
mw = 0
while mw < 4:
    print(mw * '         ' 'Shubham\'s Gaming Center|')
    mw += 1
while mw > 0:
    print(mw * '         ' 'Shubham\'s Gaming Center|')
    mw -= 1
print(10 * '--------')
input('press Enter to begin')

def Recaptcha_robocheck(Game_number):
    print(50 * '  ')
    print('I\'M NOT A ROBOT')
    print(10 * '  ')
    did_pass = 0
    robo_num = randint(1,3)
    if robo_num == 1 :
        print('|----------|     |-----------|      |----------|')
        print('| 1.Bunny  |     | 2.Racecar |      |  3.Corn  |')
        print('|----------|     |-----------|      |----------|')
        print('                                                ')
        print('|----------|     |-----------|      |----------|')
        print('| 4.Cat    |     | 5.Dog     |      |  6.Lamp  |')
        print('|----------|     |-----------|      |----------|')
        print('                                                ')
        print('|----------|     |-----------|      |----------|')
        print('| 7.Small  |     |8.Palm tree|      |  9.Lizard|')
        print('|----------|     |-----------|      |----------|')
        print('                                                ')
        recaptcha_test = input('enter the numbers of the boxes which have a name of an animal. seperate with spaces') 
        if '1' in recaptcha_test and'4' in recaptcha_test and '5' in recaptcha_test and '9' in recaptcha_test :
            did_pass = 1
    if robo_num == 2 :
        print('|----------|     |-----------|      |----------|')
        print('| 1. #     |     | 2. %      |      |  3.   #  |')
        print('|----------|     |-----------|      |----------|')
        print('                                                ')
        print('|----------|     |-----------|      |----------|')
        print('| 4.       |     | 5.        |      |  6.   &  |')
        print('|----------|     |-----------|      |----------|')
        print('                                                ')
        print('|----------|     |-----------|      |----------|')
        print('| 7.   S   |     |8.    #    |      |  9. @    |')
        print('|----------|     |-----------|      |----------|')
        print('                                                ')
        recaptcha_test = input('enter the numbers of the boxes which have hashtag. seperate with spaces') 
        if '1' in recaptcha_test and '3' in recaptcha_test and '8' in recaptcha_test:
            did_pass = 1
    if robo_num == 3 :
        print('|----------|     |-----------|      |----------|')
        print('| 1. #     |     | 2. %      |      |  3.   #  |')
        print('|----------|     |-----------|      |----------|')
        print('                                                ')
        print('|----------|     |-----------|      |----------|')
        print('| 4.       |     | 5.        |      |  6.   &  |')
        print('|----------|     |-----------|      |----------|')
        print('                                                ')
        print('|----------|     |-----------|      |----------|')
        print('| 7.   S   |     |8.         |      |  9. @    |')
        print('|----------|     |-----------|      |----------|')
        print('                                                ')
        recaptcha_test = input('enter the numbers of the boxes which have blank spaces. seperate with spaces') 
        if '4' in recaptcha_test and '5' in recaptcha_test and '8' in recaptcha_test:
            did_pass = 1
    if did_pass == 1 :
        print('you are correct press enter to continue')
        input
        return
    else:
        print('you are incorrect')
        input()
        Main_menu()
def Game_over(Game_number):
    print('\n' * 50)
    m = 0
    while m < 50 :
        print(6 * 'GAME   OVER         ')
        time.sleep(0.02)
        m += 1
    m = 0
    while m < 50 :
        print(' ')
        time.sleep(0.02)
        m += 1
    print('***************************')
    print('***************************')
    print('**                       **')
    print('**      Play again?      **')
    print('**                       **')
    print('**   \ /        |\  |    **')
    print('**    |         | \ |    **')
    print('**    |         |  \|    **')
    print('**                       **')
    print('***************************')
    print('***************************')
    yorn = input('')
    yorn = yorn.upper()
    if yorn == 'Y' :
        if Game_number == 1 :
            Army_attack()
        if Game_number == 2 :
            Car_racing()
        if Game_number == 3 :
            Treasure_hunt()
        if Game_number == 4 :
            Secret_number()
             
        
    
def Option_animator(space_number):
    mw = 0
    while mw < space_number:
        print('\n')
        time.sleep(0.05)
        mw += 1
    
mw = 0
while mw < 15:
    print('\n')
    time.sleep(0.05)
    mw += 1
mw = 0
print('RULES')
Option_animator(3)
print('There are 4 Games')
Option_animator(3)
print('Choose a game by typing its letter followed by enter')
Option_animator(3)
print('Upper case and lower case are allowed')
Option_animator(3)
print('At any time in the game type MM to return to the main menu')

input('press Enter to begin')
mw = 0
while mw < 10:
    print('\n')
    time.sleep(0.05)
    mw += 1
print('\n' * 50)
def Army_attack():
    Recaptcha_robocheck(1)
    aa = 0
    while aa < 9 :
        print('  (o) ','  ' * aa ,'           \\','  ' * (7 - aa),  '  (o)')
        print('  \|/ ','  ' * aa ,'____________)','  ' * (7 - aa),  ' \|/ ')
        print('   |  ','  ' * aa ,'            )','  ' * (7 - aa),  '  |  ')
        print('  / \ ','  ' * aa ,'           / ','  ' * (7 - aa), ' / \   ')
        time.sleep(0.25)
        print(50 * '\n')
        aa += 1
    print('ARMY ATTACK')
    Option_animator(2)
    print('Rules')
    Option_animator(2)
    print('1.The goal of the game is to survive for the longest time')
    Option_animator(2)
    print('2.You die when an enemy hits you')
    Option_animator(2)
    print('3.You can dodge arrows by using A and D keys')
    Option_animator(2)
    print('4.you can pick up a power cube and use it to kill one enemy line')
    Option_animator(2)
    input('press enter to continue')
    army_animator = 8
    you_place = 1
    while army_animator > 0 :
        if army_animator > 1 :
            print('            OOO                      ')
        if army_animator > 2 :
            print('                            ')
        if army_animator > 3 :
            print('                                         OOO                      ')
        if army_animator > 4 :
            print('                           ')
        if army_animator > 5 :
            print('                         OOO                      ')
        if army_animator > 6 :
            print('                                 ')
        if army_animator > 7 :
            print('                                ')
        you_place_input = input()
        if you_place_input == 'a':
            you_place += 1
        if you_place_input == 'd':
            you_place -= 1
        print(you_place * '  ' , 'you' )
        time.sleep(0.5)
        print('\n ' * 50)
        army_animator -= 1
    Game_over(1)
    input()
    Main_menu()
word_animator = 'on'
def type_out_word(text,speed,letters,allowed_length):
    global word_animator
    if word_animator == 'on':
        to_type_animation = text
        bb = 0
        letters_in_word = (letters - 1)
        while bb <= letters_in_word :
            if type(to_type_animation[bb]) == None:
                print('hello')    
            else:
                print(to_type_animation[bb],end = '')
            time.sleep(speed)
            bb += 1
            if allowed_length < bb:
                print('broken')
                break
    else:
        print(text)

def Car_racing():
    type_out_word('00000000000000000000\n', 0.04, 20 , 15)
    type_out_word('00000000000000000000\n', 0.04, 20 , 15)
    type_out_word('00000000000000000000\n', 0.04, 20 , 15)
    type_out_word('00000000000000000000\n', 0.04, 20 , 15)
    this = input()
    print(this)
    Recaptcha_robocheck(2)
    aa = 0
    while aa < 9 :
        print('  ' * aa ,'   /--------\     ','  ' * (7 - aa), '         /--------\    ')
        print('  ' * aa ,'  (__________\___ ','  ' * (7 - aa), '        (__________\___ ')
        print('  ' * aa ,'   o        o \   ','  ' * (7 - aa), '         o        o \   ')
        time.sleep(0.25)
        print(50 * '\n')
        aa += 1
    while aa < 14 :
        print('  ' * aa ,'   /--------\     ','  ' * aa, '         /--------\    ')
        print('  ' * aa ,'  (__________\___ ','  ' * aa, '        (__________\___ ')
        print('  ' * aa ,'   o        o \   ','  ' * aa, '         o        o \   ')
        time.sleep(0.15)
        print(50 * '\n')
        aa += 1
        print('Car Racing')
    Option_animator(2)
    print('Rules')
    Option_animator(2)
    print('1.The goal of the game is to survive for the longest time')
    Option_animator(2)
    print('2.You lose when you are hit by an obstacle')
    Option_animator(2)
    print('3.You can change lanes by pressing A and D keys')
    Option_animator(2)
    print('4.you can pick up a power boost and have immunity to one obstacle ')
    Option_animator(2)
    input('press enter to continue')
    Game_over(2)
    input()
    Main_menu()

def Treasure_hunt():
    Recaptcha_robocheck(3)
    aa = 0
    while aa < 9 :
        print('  ' * aa ,'      (o) ','  ' * (7 - aa), '    /-----\   ')
        print('  ' * aa ,'      \|/ ','  ' * (7 - aa), '   /       \  ')
        print('  ' * aa ,'      / \ ','  ' * (7 - aa), '   |_______|  ')
        time.sleep(0.25)
        print(50 * '\n')
        aa += 1
    print('  ' * aa ,'      (o) Yay I found the treasure ','  ' * (7 - aa), '    /-----\   ')
    print('  ' * aa ,'      \|/ ','  ' * (7 - aa), '                            /       \  ')
    print('  ' * aa ,'      / \ ','  ' * (7 - aa), '                            |_______|  ')
    Option_animator(2)
    print('Rules')
    Option_animator(2)
    print('1.The goal of the game is to get to the treasure')
    Option_animator(2)
    print('2.A screen will be displayed with an X indicating the location of the treasure')
    Option_animator(2)
    print('3.The X will then disappear, and you must navigate to the treasure using WASD keys')
    Option_animator(2)
    input('press enter to continue')
    input()
    play_again = 'yes'
    while True:
        target_right = randint(0, 25)
        target_forward = randint(0, 25)
        print('\n' * 50)
        print('     ' * target_right , ' \  / ')
        print('     ' * target_right , '  \/  ')
        print('     ' * target_right , '  /\  ')
        print('     ' * target_right , ' /  \ ')
        t = 0
        while t < target_forward:
            print(' ')
            t += 1
        input ('The treasure can be found at this point     Tip: you could place your mouse at that place     Press enter to continue ')
    
        print('\n' * 50)
        b = 0
        times_right = 1
        times_forward = 1
        print('\n' * 50)
        print('     ' * times_right , '  (o) ')
        print('     ' * times_right , '  \|/ ')
        print('     ' * times_right , '   |  ')
        print('     ' * times_right , '  / \ ')
        t = 0
        while t < times_forward:
            print(' ')
            t += 1
        while b < 500:
                direction = input (' which direction do you want to move in? use WASD keys to navigate')
                if direction == 'w':
                    times_forward += 1
                    print('\n' * 50)
                    print('     ' * times_right , '  (o) ')
                    print('     ' * times_right , '  \|/ ')
                    print('     ' * times_right , '   |  ')
                    print('     ' * times_right , '  / \ ')
                    t = 0
                    while t < times_forward:
                        print(' ')
                        t += 1
                elif direction ==  'd':
                    times_right += 1
                    print('\n' * 50)
                    print('     ' * times_right , '  (o) ')
                    print('     ' * times_right , '  \|/ ')
                    print('     ' * times_right , '   |  ')
                    print('     ' * times_right , '  / \ ')
                    t = 0
                    while t < times_forward:
                        print(' ')
                        t += 1
                elif direction ==  'a':
                    times_right -= 1
                    print('\n' * 50)
                    print('     ' * times_right , '  (o) ')
                    print('     ' * times_right , '  \|/ ')
                    print('     ' * times_right , '   |  ')
                    print('     ' * times_right , '  / \ ')
                    t = 0
                    while t < times_forward:
                        print(' ')
                        t += 1
                elif direction ==  's':
                    times_forward -= 1
                    print('\n' * 50)
                    print('     ' * times_right , '  (o) ')
                    print('     ' * times_right , '  \|/ ')
                    print('     ' * times_right , '   |  ')
                    print('     ' * times_right , '  / \ ')
                    t = 0
                    while t < times_forward:
                        print(' ')
                        t += 1
                elif direction ==  'mm':
                    Main_menu()
                elif direction ==  'el agua':
                    print(' security override activated')
                    print('you have found the treasure')
                    print('good job')
                    play_again = input ('do you want to play again?')
                    break
                else:
                    print(' the direction you have entered is not valid. please enter again')
                b += 1
                if target_right == times_right:
                    if target_forward == times_forward :
                        times_forward += 1
                        print('\n' * 50)
                        print('     ' * times_right , '  (o)  Yay!!!   I found a treasure')
                        print('     ' * times_right , '  \|/|---| ')
                        print('     ' * times_right , '   | |---| ')
                        print('     ' * times_right , '  / \ ')
                        t = 0
                        while t < times_forward:
                            print(' ')
                            t += 1
                        print('you have found the treasure')
                        print('good job')
                        break
        Game_over(3)
        print('good job')
        Main_menu()

def Secret_number():
    Recaptcha_robocheck(4)
    Option_animator(2)
    print('Rules')
    Option_animator(2)
    print('1.The goal of the game is to guess the correct number in the least amount of tries')
    Option_animator(2)
    input('press enter to continue')
    input()
    Random_num = str(randint(1,100))
    num_tries = 0
    Guess = 0
    while Guess != Random_num:
        Guess = input ('enter a guess ')
        if Guess > Random_num:
            print('too high ')
        elif Guess < Random_num:
            print('too low ')
        elif Guess == 'mm':
            Main_menu()
        else :
            print ('that is correct')
        num_tries = num_tries + 1
    print ('good job. you took ' , num_tries , 'tries')
    Random_num = randint(1,100)
    Game_over(4)
    Main_menu()
    
def Main_menu():
    print('Main Menu')
    print('Choose a game by typing its letter followed by enter')
    Option_animator(2)
    print('A- ARMY ATTACK')
    print('     ''  (o)             \\            (o)')
    print('     ''  \|/  ____________)           \|/ ')
    print('     ''   |               )            |  ')
    print('     ''  / \             /            / \   ')
    Option_animator(0.5)
    print('C- CAR RACING')
    print('   /--------\              /--------\    ')
    print('  (__________\___         (__________\___ ')
    print('   o        o \            o        o \   ')
    Option_animator(0.5)
    print('T- TREASURE HUNT')
    print('     ''  (o)  Yay!!!   I found a treasure')
    print('     ''  \|/|---| ')
    print('     ''   | |---| ')
    print('     ''  / \ ')
    Option_animator(0.5)
    print('S- SECRET NUMBER')
    print('     ???         ???         ???    ')
    print('    ?   ?       ?   ?       ?   ? ')
    print('         ?           ?           ?')
    print('        ?           ?           ?')
    print('       ?           ?           ?')
    print('       ?           ?           ?')
    Option_animator(0.5)
    print('Q- QUIT')

    choice = input()
    choice = choice.upper()
    if 'A' == choice:
        print('you selected ARMY ATTACK!')
        Army_attack()
    elif 'C' == choice:
        print('you selected CAR RACING!')
        Car_racing()
    elif 'T' == choice:
        print('you selected TREASURE HUNT!')
        Treasure_hunt()
    elif 'S' == choice:
        print('you selected SECRET NUMBER!')
        Secret_number()
    elif 'Q' == choice:
        print('you selected QUIT!')
    else:
        print('The option you have entered is invalid. Please try again')
        Main_menu()
Main_menu()
input()

order = 1
miss = 0
points = 0
times_forward = 7
times_forward1 = 7
times_right = randint(1,7)
times_right1 = randint(1,7)
empty = ()
you_right = 0
while True:
    action = input('     ' * you_right + '  |---|' )
    if action == 'd':
        you_right += 1
    if action == 'a':
        you_right -= 1
    if action == 'el agua':
        break
    times_forward -= 1
    times_forward1 -= 1
    if order == 1:
        print('\n' * 50)
        print('     ' * times_right1 , '  (o) 1 ')
        print('     ' * times_right1 , '  \|/ ' )
        print('     ' * times_right1 , '   |  ' )
        print('     ' * times_right1 , '  / \ ' )
        print(' \n' * 5)
        t = 0
        while t < 7:
            print(' ')
            t += 1

        print('     ' * times_right , '  (o) ')
        print('     ' * times_right , '  \|/ ' )
        print('     ' * times_right , '   |  ' )
        print('     ' * times_right , '  / \ ' )
        t = 0
        while t < times_forward:
            print(' ')
            t += 1
            
    else:
        print('\n' * 50)
        print('     ' * times_right , '  (o) ')
        print('     ' * times_right , '  \|/ ' )
        print('     ' * times_right , '   |  ' )
        print('     ' * times_right , '  / \ ' )
        t = 0
        while t < 7:
            print(' ')
            t += 1
        
        print('     ' * times_right1 , '  (o) 1 ')
        print('     ' * times_right1 , '  \|/ ' )
        print('     ' * times_right1 , '   |  ' )
        print('     ' * times_right1 , '  / \ ' )
        t = 0
        while t < times_forward1:
            print(' ')
            t += 1
        
    if times_forward == -1 or times_forward1 == -1:
        if order == 1:
            if times_right == you_right or times_right - 1 == you_right or times_right + 1 == you_right:
                print('you have been hit by 0       you have gained a point       you have ' , points)
                input
                points += 1
                if order == 1:
                    order = 0
                else:
                    order = 1
            else:
                print('you have missed')
                miss += 1
                print('you were' , you_right, 'should be' , times_right)
                print(' you have ' , miss , ' misses')
                if miss == 5:
                    print ( ' you have missed 5 times')
                    print ('game over')
                    print('your score is ' , points)
                    break
                input ()
        elif order == 0:
            if times_right1 == you_right or times_right1 - 1 == you_right or times_right1 + 1 == you_right:
                print('you have been hit by 1      you have gained a point       you have ' , points)
                input
                points += 1
                if order == 1:
                    order = 0
                else:
                    order = 1
            else:
                print('you have missed')
                miss += 1
                print('you were' , you_right, 'should be' , times_right1)
                print(' you have ' , miss , ' misses')
                if miss == 5:
                    print ( ' you have missed 5 times')
                    print ('game over')
                    print('your score is ' , points)
                    break
                input ()
        print ('order=' , order)
        input
        times_forward = 7
        times_forward1 = 7
    else:
        if times_right == 0:
            times_right = times_right + 1
        else:
            times_right = randint(times_right - 1,times_right + 1)
        if times_right1 == 0:
            times_right1 = times_right1 + 1
        else:
            times_right1 = randint(times_right1 - 1,times_right1 + 1)
highscore = 65    
print('\n' * 50)
print(' HIGHSCORES')
if points > 65:
    points = highscore
    print( 'HIGHSCORE               ' , highscore)
    print( 'Shubham                 34')
    print('you\'ve set a new highscore!!!!!')
else:
    print( 'highscore                ', highscore )  
    print( 'you                  ' , points)

while not input():
    print('ok')
print('done')
    
j = 0
lane_generator = 0
while j <= 40:
    e = 0
    while lane_generator > e :
        generate_random_obstacle()
        e += 1
    j +=1
    time.sleep(0.5)
    print( 50*'\n')
    


import shelve
d = shelve.open('score.txt')   
d['score'] = highscore           
d.close()
  
    
   


import keyboard 
while True:   
    if keyboard.interrupt('q'):   
        print('You Pressed A Key!')
        break  
