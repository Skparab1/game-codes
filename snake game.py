#snake game
import time, random
from random import randint
def clearscreen():
    print('\n'*50)
clearscreen()
autoplay = False
name = input('enter your name: ')
if name == 'autoplay':
    autoplay = True
def p(line):
    print('|'+str(line)+'|')
def printarena():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18, direction, score
    print('_'*100)
    p(l18),p(l17),p(l16),p(l15),p(l14),p(l13),p(l12),p(l11),p(l10),p(l9),p(l8),p(l7),p(l6),p(l5),p(l4),p(l3),p(l2),p(l1)
    print('_'*100)
    print('Score',score)
def removeball():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18, eraser, length
    if eraser == length and True:
        l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = l1.replace('O',' '),l2.replace('O',' '),l3.replace('O',' '),l4.replace('O',' '),l5.replace('O',' '),l6.replace('O',' '),l7.replace('O',' '),l8.replace('O',' '),l9.replace('O',' '),l10.replace('O',' '),l11.replace('O',' '),l12.replace('O',' '),l13.replace('O',' '),l14.replace('O',' '),l15.replace('O',' '),l16.replace('O',' '),l17.replace('O',' '),l18.replace('O',' ')
        eraser = 0
    eraser += 1
def removeobstacle():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18
    l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = l1.replace('#',' '),l2.replace('#',' '),l3.replace('#',' '),l4.replace('#',' '),l5.replace('#',' '),l6.replace('#',' '),l7.replace('#',' '),l8.replace('#',' '),l9.replace('#',' '),l10.replace('#',' '),l11.replace('#',' '),l12.replace('#',' '),l13.replace('#',' '),l14.replace('#',' '),l15.replace('#',' '),l16.replace('#',' '),l17.replace('#',' '),l18.replace('#',' ')
def addobstacle():
    global randheight, randpos, height, l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18
    lcont = l1 if randheight == 1 else (l2 if (randheight == 2 ) else (l3 if (randheight == 3 ) else (l4 if (randheight == 4) else (l5 if (randheight == 5) else (l6 if (randheight == 6) else (l7 if (randheight == 7) else (l8 if (randheight == 8) else (l9 if (randheight == 9) else (l10 if (randheight == 10) else (l11 if (randheight == 11) else (l12 if (randheight == 12) else (l13 if (randheight == 13) else (l14 if (randheight == 14) else (l15 if (randheight == 15) else (l16 if (randheight == 16) else (l17 if (randheight == 17) else l18))))))))))))))))
    linepart1 = lcont[:randpos-1]
    linepart2 = lcont[randpos:]
    line = linepart1 + '#' + linepart2
    l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = (line if randheight == 1 else l1),(line if randheight == 2 else l2),(line if randheight == 3 else l3),(line if randheight == 4 else l4),(line if randheight == 5 else l5),(line if randheight == 6 else l6),(line if randheight == 7 else l7),(line if randheight == 8 else l8),(line if randheight == 9 else l9),(line if randheight == 10 else l10),(line if randheight == 11 else l11),(line if randheight == 12 else l12),(line if randheight == 13 else l13),(line if randheight == 14 else l14),(line if randheight == 15 else l15),(line if randheight == 16 else l16),(line if randheight == 17 else l17),(line if randheight == 18 else l18)
def addball(line):
    global pos
    linepart1 = line[:pos-1]
    linepart2 = line[pos:]
    line = linepart1 + 'O' + linepart2
    return line
pos = 50
eraser = 1
randpos = randint(2,98)
randheight = randint(2,17)
l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = ' '*99,' '*99,' '*99,' '*99,' '*99,' '*99,' '*99,' '*99,' '*99,' '*99,((' '*8)+'O'+(' '*90)),' '*99,' '*99,' '*99,' '*99,' '*99,' '*99,' '*99
addobstacle()
score = 0
direction = 'right'
turningmode = False
length = 1
height = 11
while True:
    try:
        if direction == 'right' or direction == 'left':
            time.sleep(0.1)
        else:
            time.sleep(0.15)
        printarena()
        ln = height #ln = 1 if ('o' in l1 ) else (2 if ('o' in l2 ) else (3 if ('o' in l3 ) else (4 if ('o' in l4 ) else (5 if ('o' in l5 ) else (6 if ('o' in l6 ) else (7 if ('o' in l7 ) else (8 if ('o' in l8 ) else (9 if ('o' in l9 ) else (10 if ('o' in l10 ) else (11 if ('o' in l11 ) else (12 if ('o' in l12 ) else (13 if ('o' in l13 ) else (14 if ('o' in l14 ) else (15 if ('o' in l15 ) else (16 if ('o' in l16 ) else (17 if ('o' in l17 ) else 18))))))))))))))))
        if turningmode == True:
            blank = ''
            #turn
        else:
            ln = height
            #ln = 1 if ('o' in l1 ) else (2 if ('o' in l2 ) else (3 if ('o' in l3 ) else (4 if ('o' in l4 ) else (5 if ('o' in l5 ) else (6 if ('o' in l6 ) else (7 if ('o' in l7 ) else (8 if ('o' in l8 ) else (9 if ('o' in l9 ) else (10 if ('o' in l10 ) else (11 if ('o' in l11 ) else (12 if ('o' in l12 ) else (13 if ('o' in l13 ) else (14 if ('o' in l14 ) else (15 if ('o' in l15 ) else (16 if ('o' in l16 ) else (17 if ('o' in l17 ) else 18))))))))))))))))
            if direction == 'right':
                removeball()
                pos = pos + 1
                l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = (addball(l1) if ln == 1 else l1),(addball(l2) if ln == 2 else l2),(addball(l3) if ln == 3 else l3),(addball(l4) if ln == 4 else l4),(addball(l5) if ln == 5 else l5),(addball(l6) if ln == 6 else l6),(addball(l7) if ln == 7 else l7),(addball(l8) if ln == 8 else l8),(addball(l9) if ln == 9 else l9),(addball(l10) if ln == 10 else l10),(addball(l11) if ln == 11 else l11),(addball(l12) if ln == 12 else l12),(addball(l13) if ln == 13 else l13),(addball(l14) if ln == 14 else l14),(addball(l15) if ln == 15 else l15),(addball(l16) if ln == 16 else l16),(addball(l17) if ln == 17 else l17),(addball(l18) if ln == 18 else l18)
            if direction == 'left':
                removeball()
                pos = pos - 1
                l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = (addball(l1) if ln == 1 else l1),(addball(l2) if ln == 2 else l2),(addball(l3) if ln == 3 else l3),(addball(l4) if ln == 4 else l4),(addball(l5) if ln == 5 else l5),(addball(l6) if ln == 6 else l6),(addball(l7) if ln == 7 else l7),(addball(l8) if ln == 8 else l8),(addball(l9) if ln == 9 else l9),(addball(l10) if ln == 10 else l10),(addball(l11) if ln == 11 else l11),(addball(l12) if ln == 12 else l12),(addball(l13) if ln == 13 else l13),(addball(l14) if ln == 14 else l14),(addball(l15) if ln == 15 else l15),(addball(l16) if ln == 16 else l16),(addball(l17) if ln == 17 else l17),(addball(l18) if ln == 18 else l18)
            if direction == 'up':
                height += 1
                removeball()
                l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l6,l17,l18 = (addball(l2) if ln == 1 else l2),(addball(l3) if ln == 2 else l3),(addball(l4) if ln == 3 else l4),(addball(l5) if ln == 4 else l5),(addball(l6) if ln == 5 else l6),(addball(l7) if ln == 6 else l7),(addball(l8) if ln == 7 else l8),(addball(l9) if ln == 8 else l9),(addball(l10) if ln == 9 else l10),(addball(l11) if ln == 10 else l11),(addball(l12) if ln == 11 else l12),(addball(l13) if ln == 12 else l13),(addball(l14) if ln == 13 else l14),(addball(l15) if ln == 14 else l15),(addball(l16) if ln == 15 else l16),(addball(l17) if ln == 16 else l17),(addball(l18) if ln == 17 else l18)
            if direction == 'down':
                height -= 1
                removeball()
                l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l6,l17 = (addball(l1) if ln == 2 else l1),(addball(l2) if ln == 3 else l2),(addball(l3) if ln == 4 else l3),(addball(l4) if ln == 5 else l4),(addball(l5) if ln == 6 else l5),(addball(l6) if ln == 7 else l6),(addball(l7) if ln == 8 else l7),(addball(l8) if ln == 9 else l8),(addball(l9) if ln == 10 else l9),(addball(l10) if ln == 11 else l10),(addball(l11) if ln == 12 else l11),(addball(l12) if ln == 13 else l12),(addball(l13) if ln == 14 else l13),(addball(l14) if ln == 15 else l14),(addball(l15) if ln == 16 else l15),(addball(l16) if ln == 17 else l16),(addball(l17) if ln == 18 else l17)
            if pos >= 100 or pos <= 0 or height >= 19 or height <= -1:
                print('you have crashed into the wall')
                break
            if height == randheight and pos == randpos:
                score += 1
                removeobstacle()
                randpos = randint(2,98)
                randheight = randint(2,17)
                addobstacle()
                length += 1
            lcont = l1 if ('o' in l1 ) else (l2 if ('o' in l2 ) else (l3 if ('o' in l3 ) else (l4 if ('o' in l4 ) else (l5 if ('o' in l5 ) else (l6 if ('o' in l6 ) else (l7 if ('o' in l7 ) else (l8 if ('o' in l8 ) else (l9 if ('o' in l9 ) else (l10 if ('o' in l10 ) else (l11 if ('o' in l11 ) else (l12 if ('o' in l12 ) else (l13 if ('o' in l13 ) else (l14 if ('o' in l14 ) else (l15 if ('o' in l15 ) else (l16 if ('o' in l16 ) else (l17 if ('o' in l17 ) else l18))))))))))))))))
            if lcont[pos] == 'O':
                print('You have hit yourself')
                break
            if autoplay == True:
                raise ValueError
            #if direction == 'up':
                #l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = (removeball(l1) if ln == 1 else l1), (removeball(l2) if ln == 2 else l2),(removeball(l3) if ln == 3 else l3),(removeball(l4) if ln == 4 else l4),(removeball(l5) if ln == 5 else l5),(removeball(l6) if ln == 6 else (addball if ln == 1 else l6)),(removeball(l7) if ln == 7 else (addball if ln == 2 else l7)),(removeball(l8) if ln == 8 else (addball if ln == 3 else l8)),(removeball(l9) if ln == 9 else (addball if ln == 4 else l9)),(removeball(l10) if ln == 10 else (addball if ln == 5 else l10)),(removeball(l11) if ln == 11 else (addball if ln == 6 else l11)),(removeball(l12) if ln == 12 else (addball if ln == 7 else l12)),(removeball(l13) if ln == 13 else (addball if ln == 8 else l13)),(removeball(l14) if ln == 14 else (addball if ln == 9 else l14)),(removeball(l15) if ln == 15 else (addball if ln == 10 else l15)),(removeball(l16) if ln == 16 else (addball if ln == 11 else l16)),(removeball(l17) if ln == 17 else (addball if ln == 12 else l17)),(removeball(18) if ln == 18 else (addball if ln == 13 else l18))
            #if direction == 'down':
                #l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = (addball(l1) if ln == 1 else l1),(addball(l2) if ln == 2 else l2),(addball(l3) if ln == 3 else l3),(addball(l4) if ln == 4 else l4),(addball(l5) if ln == 5 else l5),(addball(l6) if ln == 6 else (removeball if ln == 1 else l6)),(addball(l7) if ln == 7 else (removeball if ln == 2 else l7)),(addball(l8) if ln == 8 else (removeball if ln == 3 else l8)),(addball(l9) if ln == 9 else (removeball if ln == 4 else l9)),(addball(l10) if ln == 10 else (removeball if ln == 5 else l10)),(addball(l11) if ln == 11 else (removeball if ln == 6 else l11)),(addball(l12) if ln == 12 else (removeball if ln == 7 else l12)),(addball(l13) if ln == 13 else (removeball if ln == 8 else l13)),(addball(l14) if ln == 14 else (removeball if ln == 9 else l14)),(addball(l15) if ln == 15 else (removeball if ln == 10 else l15)),(addball(l16) if ln == 16 else (removeball if ln == 11 else l16)),(addball(l17) if ln == 17 else (removeball if ln == 12 else l17)),(addball(l18) if ln == 18 else (removeball if ln == 13 else l18))
    except:
        #ln = 1 if ('o' in l1 ) else (2 if ('o' in l2 ) else (3 if ('o' in l3 ) else (4 if ('o' in l4 ) else (5 if ('o' in l5 ) else (6 if ('o' in l6 ) else (7 if ('o' in l7 ) else (8 if ('o' in l8 ) else (9 if ('o' in l9 ) else (10 if ('o' in l10 ) else (11 if ('o' in l11 ) else (12 if ('o' in l12 ) else (13 if ('o' in l13 ) else (14 if ('o' in l14 ) else (15 if ('o' in l15 ) else (16 if ('o' in l16 ) else (17 if ('o' in l17 ) else 18))))))))))))))))
        #lcont = l1 if ('o' in l1 ) else (l2 if ('o' in l2 ) else (l3 if ('o' in l3 ) else (l4 if ('o' in l4 ) else (l5 if ('o' in l5 ) else (l6 if ('o' in l6 ) else (l7 if ('o' in l7 ) else (l8 if ('o' in l8 ) else (l9 if ('o' in l9 ) else (l10 if ('o' in l10 ) else (l11 if ('o' in l11 ) else (l12 if ('o' in l12 ) else (l13 if ('o' in l13 ) else (l14 if ('o' in l14 ) else (l15 if ('o' in l15 ) else (l16 if ('o' in l16 ) else (l17 if ('o' in l17 ) else l18))))))))))))))))
        #lcontbelow = l1 if ('o' in l1 ) else (l1 if ('o' in l2 ) else (l2 if ('o' in l3 ) else (l4 if ('o' in l5 ) else (l5 if ('o' in l6 ) else (l6 if ('o' in l7 ) else (l7 if ('o' in l8 ) else (l8 if ('o' in l9 ) else (l9 if ('o' in l10 ) else (l10 if ('o' in l11 ) else (l11 if ('o' in l12 ) else (l12 if ('o' in l13 ) else (l13 if ('o' in l14 ) else (l14 if ('o' in l15 ) else (l15 if ('o' in l16 ) else (l16 if ('o' in l17 ) else (l17 if ('o' in l18 ) else l18))))))))))))))))
        #lcontabove = l2 if ('o' in l1 ) else (l3 if ('o' in l2 ) else (l4 if ('o' in l3 ) else (l5 if ('o' in l4 ) else (l6 if ('o' in l5 ) else (l7 if ('o' in l6 ) else (l8 if ('o' in l7 ) else (l9 if ('o' in l8 ) else (l10 if ('o' in l9 ) else (l11 if ('o' in l10 ) else (l12 if ('o' in l11 ) else (l13 if ('o' in l12 ) else (l14 if ('o' in l13 ) else (l15 if ('o' in l14 ) else (l16 if ('o' in l15 ) else (l16 if ('o' in l16 ) else (l18 if ('o' in l17 ) else l18))))))))))))))))
        if True:
            if direction == 'right' or direction == 'left':
                if randheight <= height:
                    direction = 'down'
                else:
                    direction = 'up'
            else:
                if randpos <= pos:
                    direction = 'left'
                else:
                    direction = 'right'
print('you have lost')