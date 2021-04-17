spaces = 65
spaces1 = 45
score = 0
successjump = 0
failjump = 0
high = 0000
speed = 0.05
newscore = False
import shelve
"""reader = shelve.open('dino1stplace.txt')   
reader['dino1stplace'] = '1000'       
reader.close()
reader = shelve.open('dino2ndplace.txt')   
reader['dino2ndplace'] = '500'       
reader.close()
reader = shelve.open('dino3rdplace.txt')   
reader['dino3rdplace'] = '250'       
reader.close()
reader = shelve.open('dino4thplace.txt')   
reader['dino4thplace'] = '120'       
reader.close()
reader = shelve.open('dino5thplace.txt')   
reader['dino5thplace'] = '60'       
reader.close()
reader = shelve.open('dino1stname.txt')   
reader['dino1stname'] = 'Bunny'       
reader.close()
reader = shelve.open('dino2ndname.txt')   
reader['dino2ndname'] = 'Fishy'       
reader.close()
reader = shelve.open('dino3rdname.txt')   
reader['dino3rdname'] = 'Doggy'       
reader.close()
reader = shelve.open('dino4thname.txt')   
reader['dino4thname'] = 'Shubham'       
reader.close()
reader = shelve.open('dino5thname.txt')   
reader['dino5thname'] = 'Hoss'       
reader.close()"""
def length_of_text(text):
    text = text + '∞'
    letter_number = 0
    letter = ' '
    while letter != '∞':
        letter = text[letter_number]
        letter_number += 1
    letter_number = letter_number - 1
    return letter_number   
name = input('Enter your name ')
import time
from random import randint
random_num = randint(1,12)
random_num = str(random_num)
random_obj1 = ('/-\ ' if random_num == '1' else ('<->' if random_num == '2' else ('(-)' if random_num == '3' else ('^^^' if random_num == '4' else ('=+=' if random_num == '5' else ('|-|' if random_num == '6' else ('{-}' if random_num == '7' else (']-[' if random_num == '8' else ('-#-' if random_num == '9' else ('@-@' if random_num == '10' else ('*-*' if random_num == '11' else ('~+~' if random_num == '12' else ('!-!' if random_num == '13' else '???')))))))))))))
random_num = randint(1,12)
random_num = str(random_num)
random_obj2 = ('/-\ ' if random_num == '1' else ('<->' if random_num == '2' else ('(-)' if random_num == '3' else ('^^^' if random_num == '4' else ('=+=' if random_num == '5' else ('|-|' if random_num == '6' else ('{-}' if random_num == '7' else (']-[' if random_num == '8' else ('-#-' if random_num == '9' else ('@-@' if random_num == '10' else ('*-*' if random_num == '11' else ('~+~' if random_num == '12' else ('!-!' if random_num == '13' else '???')))))))))))))
if random_obj1 == random_obj2:
    random_obj2 =   ('/-\ ' if random_num == '1' else ('<->' if random_num == '2' else ('(-)' if random_num == '3' else ('^^^' if random_num == '4' else ('=+=' if random_num == '5' else ('|-|' if random_num == '6' else ('{-}' if random_num == '7' else (']-[' if random_num == '8' else ('-#-' if random_num == '9' else ('@-@' if random_num == '10' else ('*-*' if random_num == '11' else ('~+~' if random_num == '12' else ('!-!' if random_num == '13' else '???')))))))))))))
first_obj = random_obj1
second_obj = random_obj2
while True:
    try:
        if first_obj == random_obj1:
            firstspaces = spaces
            secondspaces = spaces1
        else:
            firstspaces = spaces1
            secondspaces = spaces
        print('score: ', score,'\n                     YOU', firstspaces * ' ', first_obj, secondspaces * ' ', second_obj)
        score += 1
        speed = speed - 0.00005
        if speed <= 0.00009:
            speed = 0.00008
        time.sleep(speed)
        print('\n' * 50)
        if first_obj == random_obj1:
            spaces -= 1
        else:
            spaces1 -= 1
        if spaces <= -6 or spaces1 <= -6: 
            print('You lose.\nScore: ', score, ' points')
            print('Successful jumps: ', successjump, '       Fail jumps: ', failjump) 
            break
    except(KeyboardInterrupt,SystemExit):
        if spaces <= 3:
            successjump += 1
            print('\n' * 50)
            print('score: ', score,'\n                     YOU\n                        ', random_obj1, spaces1 * ' ', random_obj2)
            score += 1
            time.sleep(speed)
            print('\n' * 50)
            spaces -= 1
            print('score: ', score,'\n                     YOU\n\n                     ', random_obj1, spaces1 * ' ', random_obj2)
            score += 1
            time.sleep(speed)
            print('\n' * 50)
            spaces -= 1
            print('score: ', score,'\n                     YOU\n\n\n                  ', random_obj1, spaces1 * ' ', random_obj2)
            score += 1
            time.sleep(speed)
            print('\n' * 50)
            spaces -= 1
            print('score: ', score,'\n                     YOU\n\n                  ', random_obj1, spaces1 * ' ', random_obj2)
            score += 1
            time.sleep(speed)
            print('\n' * 50)
            spaces -= 1
            print('score: ', score,'\n                     YOU\n                   ', random_obj1, spaces1 * ' ', random_obj2)
            score += 1
            time.sleep(speed)
            print('\n' * 50)
            spaces -= 1
            spaces = 15
            while spaces >= 0:
                print('score: ', score,'\n',spaces * ' ', random_obj1, (15 - spaces) * ' ', 'YOU', spaces1 * ' ', random_obj2)
                time.sleep(speed)
                score += 1
                print('\n' * 50)
                spaces -= 1
                spaces1 -= 1
            spaces = 65
            random_num = randint(1,12)
            random_num = str(random_num)
            random_obj1 =   ('/-\ ' if random_num == '1' else ('<->' if random_num == '2' else ('(-)' if random_num == '3' else ('^^^' if random_num == '4' else ('=+=' if random_num == '5' else ('|-|' if random_num == '6' else ('{-}' if random_num == '7' else (']-[' if random_num == '8' else ('-#-' if random_num == '9' else ('@-@' if random_num == '10' else ('*-*' if random_num == '11' else ('~+~' if random_num == '12' else ('!-!' if random_num == '13' else '???')))))))))))))
            if random_obj1 == random_obj2:
                random_obj1 =   ('/-\ ' if random_num == '1' else ('<->' if random_num == '2' else ('(-)' if random_num == '3' else ('^^^' if random_num == '4' else ('=+=' if random_num == '5' else ('|-|' if random_num == '6' else ('{-}' if random_num == '7' else (']-[' if random_num == '8' else ('-#-' if random_num == '9' else ('@-@' if random_num == '10' else ('*-*' if random_num == '11' else ('~+~' if random_num == '12' else ('!-!' if random_num == '13' else '???')))))))))))))
            first_obj = random_obj2
            second_obj = random_obj1
        elif spaces1 <= 3:
            successjump += 1
            print('\n' * 50)
            print('score: ', score,'\n                     YOU\n                        ', random_obj2, spaces * ' ', random_obj1)
            time.sleep(speed)
            score += 1
            print('\n' * 50)
            spaces1 -= 1
            print('score: ', score,'\n                     YOU\n\n                     ', random_obj2, spaces * ' ', random_obj1)
            time.sleep(speed)
            score += 1
            print('\n' * 50)
            spaces1 -= 1
            print('score: ', score,'\n                     YOU\n\n\n                  ', random_obj2, spaces * ' ', random_obj1)
            time.sleep(speed)
            score += 1
            print('\n' * 50)
            spaces1 -= 1
            print('score: ', score,'\n                     YOU\n\n                  ', random_obj2, spaces * ' ', random_obj1)
            time.sleep(speed)
            score += 1
            print('\n' * 50)
            spaces1 -= 1
            print('score: ', score,'\n                     YOU\n                   ', random_obj2, spaces * ' ', random_obj1)
            time.sleep(speed)
            score += 1
            print('\n' * 50)
            spaces1 -= 1
            spaces1 = 15
            while spaces1 >= 0:
                print('score: ', score,'\n',spaces1 * ' ', random_obj2, (15 - spaces1) * ' ', 'YOU', spaces * ' ', random_obj1)
                time.sleep(speed)
                score += 1
                print('\n' * 50)
                spaces1 -= 1
                spaces -= 1
            spaces1 = 65
            random_num = randint(1,12)
            random_num = str(random_num)
            random_obj2 =   ('/-\ ' if random_num == '1' else ('<->' if random_num == '2' else ('(-)' if random_num == '3' else ('^^^' if random_num == '4' else ('=+=' if random_num == '5' else ('|-|' if random_num == '6' else ('{-}' if random_num == '7' else (']-[' if random_num == '8' else ('-#-' if random_num == '9' else ('@-@' if random_num == '10' else ('*-*' if random_num == '11' else ('~+~' if random_num == '12' else ('!-!' if random_num == '13' else '???')))))))))))))
            if random_obj1 == random_obj2:
                random_obj2 =   ('/-\ ' if random_num == '1' else ('<->' if random_num == '2' else ('(-)' if random_num == '3' else ('^^^' if random_num == '4' else ('=+=' if random_num == '5' else ('|-|' if random_num == '6' else ('{-}' if random_num == '7' else (']-[' if random_num == '8' else ('-#-' if random_num == '9' else ('@-@' if random_num == '10' else ('*-*' if random_num == '11' else ('~+~' if random_num == '12' else ('!-!' if random_num == '13' else '???')))))))))))))
            first_obj = random_obj1
            second_obj = random_obj2
        else:
            failjump += 1
            print('score: ', score,'\n                     n?\n                        ', spaces1 * ' ', random_obj1, spaces1 * ' ', random_obj2)
            time.sleep(speed)
            print('\n' * 50)
            score += 1
            spaces -= 1
            print('score: ', score,'\n                     YOU\n\n                        ', spaces * ' ', random_obj1, spaces1 * ' ', random_obj2)
            time.sleep(speed)
            score += 1
            print('\n' * 50)
            spaces -= 1
            print('score: ', score,'\n                     YOU\n\n\n                        ', spaces * ' ', random_obj1, spaces1 * ' ', random_obj2)
            time.sleep(speed)
            score += 1
            print('\n' * 50)
            spaces -= 1
            print('score: ', score,'\n                     YOU\n\n                        ', spaces * ' ', random_obj1, spaces1 * ' ', random_obj2)
            time.sleep(speed)
            score += 1
            print('\n' * 50)
            spaces -= 1
            print('score: ', score,'\n                     YOU\n                        ', spaces * ' ', random_obj1, spaces1 * ' ', random_obj2)
            time.sleep(speed)
            score += 1
            print('\n' * 50)
            spaces -= 1
score = str(score)
d = shelve.open('dinoallscores.txt')
allhigh = d['dinoallscores']
d.close()
allhigh = allhigh + '\n' + name + '     '+ score +'          '
if name == 'erase all':
    reader = shelve.open('dinoallscores.txt')   
    reader['dinoallscores'] = ' '       
    reader.close()
    name = ''
    score = ''
else:
    reader = shelve.open('dinoallscores.txt')   
    reader['dinoallscores'] = allhigh       
    reader.close()  
while True:
    try:
        print('You lose.\nScore: ', score, ' points')
        print('Successful jumps: ', successjump, '       Fail jumps: ', failjump) 
        print('\nGreat job!')
        print('View the scores below:\n\n')
        d = shelve.open('dinoallscores.txt')
        allhigh = d['dinoallscores']
        d.close()
        print('Player                  Score'), print(allhigh)
        if score > high:
            d = shelve.open('dino1stplace.txt')
            oldhigh = d['dino1stplace']
            d.close()
            d = shelve.open('dino1stname.txt')
            oldname = d['dino1stname']
            d.close()
            print('YOU have beaten ', oldname,'\'s highscore of ', oldhigh)
            print('YOU ARE THE NEW HIGHSCORE!!!')
        elif score == high:
            d = shelve.open('dino1stplace.txt')
            oldhigh = d['dino1stplace']
            d.close()
            d = shelve.open('din1stname.txt')
            oldname = d['dino1stname']
            d.close()
            print('YOU have met ',oldname,'\'s HIGHSCORE of ', oldhigh)
        else:
            d = shelve.open('dino1stplace.txt')
            oldhigh = d['dino1stplace']
            d.close()
            d = shelve.open('dino1stname.txt')
            oldname = d['dino1stname']
            d.close()
            print('Try to beat',oldname,'\'s HIGHSCORE of ', oldhigh)
        print('leaderboard:')
        d = shelve.open('dino1stplace.txt')
        place1 = d['dinoallscores']
        d.close()
        d = shelve.open('dino2ndplace.txt')
        place2 = d['dinoallscores']
        d.close()
        d = shelve.open('dino3rdplace.txt')
        place3 = d['dinoallscores']
        d.close()
        d = shelve.open('dino4thplace.txt')
        place4 = d['dinoallscores']
        d.close()
        d = shelve.open('dino5thplace.txt')
        place5 = d['dinoallscores']
        d.close()
        if score >= place1:
            break
    except(KeyboardInterrupt,SystemExit):
        print('\n' * 50)