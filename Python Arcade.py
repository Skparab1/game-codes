# Python Arcade (game compilation)
#Import all
import time, random, shelve
from random import randint, randrange

# shelving defs
def shelvewrite(textfilename,towrite): #write to text file
    textfilenametxt = textfilename + '.txt'
    writer = shelve.open(str(textfilenametxt))
    writer[str(textfilename)] = towrite
    writer.close()
def shelveread(textfilename): # read form text file
    textfilenametxt = textfilename + '.txt'
    reader = shelve.open(str(textfilenametxt))
    text = reader[str(textfilename)]
    reader.close()
    return text
def shelveappend(textfilename, toappend): #append to text file
    textfilenametxt = textfilename + '.txt'
    read = shelveread(textfilename)
    toappend = str(toappend) + str(read)
    shelvewrite(textfilename, toappend)
def clearscreen(): 
    print('\n' * 50)

# defs for pong
def addmidline(line):
    return line[:49] + '|' + line[50:]
def printarena(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18):
    global p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18, name
    print('\n'*50),print('Pypong Pro (computer)'+(' '*70)+name),print(' '+('_'*100))
    print(s18+addmidline(line18)+p18),print(s17+addmidline(line17)+p17),print(s16+addmidline(line16)+p16),print(s15+addmidline(line15)+p15),print(s14+addmidline(line14)+p14),print(s13+addmidline(line13)+p13),print(s12+addmidline(line12)+p12),print(s11+addmidline(line11)+p11),print(s10+addmidline(line10)+p10),print(s9+addmidline(line9)+p9),print(s8+addmidline(line8)+p8),print(s7+addmidline(line7)+p7),print(s6+addmidline(line6)+p6),print(s5+addmidline(line5)+p5),print(s4+addmidline(line4)+p4),print(s3+addmidline(line3)+p3),print(s2+addmidline(line2)+p2),print(s1+addmidline(line1)+p1)
    print(' '+('-'*100))
def removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18):
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('o',' '),line2.replace('o',' '),line3.replace('o',' '),line4.replace('o',' '),line5.replace('o',' '),line6.replace('o',' '),line7.replace('o',' '),line8.replace('o',' '),line9.replace('o',' '),line10.replace('o',' '),line11.replace('o',' '),line12.replace('o',' '),line13.replace('o',' '),line14.replace('o',' '),line15.replace('o',' '),line16.replace('o',' '),line17.replace('o',' '),line18.replace('o',' ')
    return line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
def addball(pos,line):
    linepart1 = line[:pos-1]
    linepart2 = line[pos+1:]
    line = linepart1 + 'o ' + linepart2
    return line
def moveball(movedirection,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18):
    global pos, angle
    linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    numtomove = angle
    if movedirection == 'right':
        pos += numtomove
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 1 else line1),(addball(pos,line2) if linenum == 2 else line2),(addball(pos,line3) if linenum == 3 else line3),(addball(pos,line4) if linenum == 4 else line4),(addball(pos,line5) if linenum == 5 else line5),(addball(pos,line6) if linenum == 6 else line6),(addball(pos,line7) if linenum == 7 else line7),(addball(pos,line8) if linenum == 8 else line8),(addball(pos,line9) if linenum == 9 else line9),(addball(pos,line10) if linenum == 10 else line10),(addball(pos,line11) if linenum == 11 else line11),(addball(pos,line12) if linenum == 12 else line12),(addball(pos,line13) if linenum == 13 else line13),(addball(pos,line14) if linenum == 14 else line14),(addball(pos,line15) if linenum == 15 else line15),(addball(pos,line16) if linenum == 16 else line16),(addball(pos,line17) if linenum == 17 else line17),(addball(pos,line18) if linenum == 18 else line18)
    if movedirection == 'left':
        pos -= numtomove
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 1 else line1),(addball(pos,line2) if linenum == 2 else line2),(addball(pos,line3) if linenum == 3 else line3),(addball(pos,line4) if linenum == 4 else line4),(addball(pos,line5) if linenum == 5 else line5),(addball(pos,line6) if linenum == 6 else line6),(addball(pos,line7) if linenum == 7 else line7),(addball(pos,line8) if linenum == 8 else line8),(addball(pos,line9) if linenum == 9 else line9),(addball(pos,line10) if linenum == 10 else line10),(addball(pos,line11) if linenum == 11 else line11),(addball(pos,line12) if linenum == 12 else line12),(addball(pos,line13) if linenum == 13 else line13),(addball(pos,line14) if linenum == 14 else line14),(addball(pos,line15) if linenum == 15 else line15),(addball(pos,line16) if linenum == 16 else line16),(addball(pos,line17) if linenum == 17 else line17),(addball(pos,line18) if linenum == 18 else line18)
    if movedirection == 'rightup':
        pos = pos + numtomove                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line2) if linenum == 1 else line2),(addball(pos,line3) if linenum == 2 else line3),(addball(pos,line4) if linenum == 3 else line4),(addball(pos,line5) if linenum == 4 else line5),(addball(pos,line6) if linenum == 5 else line6),(addball(pos,line7) if linenum == 6 else line7),(addball(pos,line8) if linenum == 7 else line8),(addball(pos,line9) if linenum == 8 else line9),(addball(pos,line10) if linenum == 9 else line10),(addball(pos,line11) if linenum == 10 else line11),(addball(pos,line12) if linenum == 11 else line12),(addball(pos,line13) if linenum == 12 else line13),(addball(pos,line14) if linenum == 13 else line14),(addball(pos,line15) if linenum == 14 else line15),(addball(pos,line16) if linenum == 15 else line16),(addball(pos,line17) if linenum == 16 else line17),(addball(pos,line18) if linenum == 17 else line18)
    if movedirection== 'leftup':
        pos = pos - numtomove                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line2) if linenum == 1 else line2),(addball(pos,line3) if linenum == 2 else line3),(addball(pos,line4) if linenum == 3 else line4),(addball(pos,line5) if linenum == 4 else line5),(addball(pos,line6) if linenum == 5 else line6),(addball(pos,line7) if linenum == 6 else line7),(addball(pos,line8) if linenum == 7 else line8),(addball(pos,line9) if linenum == 8 else line9),(addball(pos,line10) if linenum == 9 else line10),(addball(pos,line11) if linenum == 10 else line11),(addball(pos,line12) if linenum == 11 else line12),(addball(pos,line13) if linenum == 12 else line13),(addball(pos,line14) if linenum == 13 else line14),(addball(pos,line15) if linenum == 14 else line15),(addball(pos,line16) if linenum == 15 else line16),(addball(pos,line17) if linenum == 16 else line17),(addball(pos,line18) if linenum == 17 else line18)
    if movedirection == 'rightdown':
        pos = pos + numtomove                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 2 else line1),(addball(pos,line2) if linenum == 3 else line2),(addball(pos,line3) if linenum == 4 else line3),(addball(pos,line4) if linenum == 5 else line4),(addball(pos,line5) if linenum == 6 else line5),(addball(pos,line6) if linenum == 7 else line6),(addball(pos,line7) if linenum == 8 else line7),(addball(pos,line8) if linenum == 9 else line8),(addball(pos,line9) if linenum == 10 else line9),(addball(pos,line10) if linenum == 11 else line10),(addball(pos,line11) if linenum == 12 else line11),(addball(pos,line12) if linenum == 13 else line12),(addball(pos,line13) if linenum == 14 else line13),(addball(pos,line14) if linenum == 15 else line14),(addball(pos,line15) if linenum == 16 else line15),(addball(pos,line16) if linenum == 17 else line16),(addball(pos,line17) if linenum == 18 else line17),(addball(pos,line18) if linenum == False else line18)
    if movedirection == 'leftdown':
        pos = pos - numtomove                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = removeball(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(pos,line1) if linenum == 2 else line1),(addball(pos,line2) if linenum == 3 else line2),(addball(pos,line3) if linenum == 4 else line3),(addball(pos,line4) if linenum == 5 else line4),(addball(pos,line5) if linenum == 6 else line5),(addball(pos,line6) if linenum == 7 else line6),(addball(pos,line7) if linenum == 8 else line7),(addball(pos,line8) if linenum == 9 else line8),(addball(pos,line9) if linenum == 10 else line9),(addball(pos,line10) if linenum == 11 else line10),(addball(pos,line11) if linenum == 12 else line11),(addball(pos,line12) if linenum == 13 else line12),(addball(pos,line13) if linenum == 14 else line13),(addball(pos,line14) if linenum == 15 else line14),(addball(pos,line15) if linenum == 16 else line15),(addball(pos,line16) if linenum == 17 else line16),(addball(pos,line17) if linenum == 18 else line17),(addball(pos,line18) if linenum == False else line18)
    return line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18

#defs for flappy bird
def addbird(line):
    line = '(0)>' + line[4:]
    return line
# defs for crossy road
def printlanes(content1, b1, content2, b2, content3, b3, first):
    print('-'*125), print(b3), print(b3), print('-'*125), print(content3), print(content3),print('-'*125),print(b2),print(b2),print('-'*125),print(content2), print(content2), print('-'*125),print(b1),print(b1),print('-'*125),print(content1), print(content1), print('-'*125), print(first),print(first)
def refreshlanecontent(newcontent, lanecontent):
    global lost
    numtoadd = randint(0,2)
    lanecontent = str(lanecontent)
    dellanes = (-1 * numtoadd) - 1 
    savecontent = lanecontent[0:dellanes]
    lanecontent = (numtoadd * ' ') + str(newcontent) + str(savecontent)
    if '(' in lanecontent:
        try:
            if lanecontent[64] != ' ' or lanecontent[65] != ' ':
                lost = True
        except:
            blank = ''
        lanecontent = removeguyfromlane(lanecontent)
        lanecontent = addguytolanecontent(lanecontent)
    if len(lanecontent) >= 125:
        lanecontent = lanecontent[0:125]
    return lanecontent
def removeguyfromlane(lanecontent):
    lane = lanecontent.replace('(--)','')
    return lane
def addguytolanecontent(lanecontent):
    firstpart = lanecontent[0:65]
    secondpart = lanecontent[65:]
    final = firstpart + '(--)' + secondpart
    return final

#defs for dino game
def length_of_text(text):
    text = text + '∞'
    letter_number = 0
    letter = ' '
    while letter != '∞':
        letter = text[letter_number]
        letter_number += 1
    letter_number = letter_number - 1
    return letter_number  

#defs for snake game
def p(line):
    print('|'+str(line)+'|')
def printarenasnake():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18, direction, score
    print('_'*100)
    p(l18),p(l17),p(l16),p(l15),p(l14),p(l13),p(l12),p(l11),p(l10),p(l9),p(l8),p(l7),p(l6),p(l5),p(l4),p(l3),p(l2),p(l1)
    print('_'*100)
    print('Score',score)
def removeballsnake():
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
def addballsnake(line):
    global pos
    linepart1 = line[:pos-1]
    linepart2 = line[pos:]
    line = linepart1 + 'O' + linepart2
    return line
#defs for treasure hunt
def treasure_hunt():
    print('Rules')
    print('1.The goal of the game is to get to the treasure')
    print('2.A screen will be displayed with an X indicating the location of the treasure')
    print('3.The X will then disappear, and you must navigate to the treasure using WASD keys')
    input('press enter to continue')
    while True:
        target_right = randint(0, 25)
        target_forward = randint(0, 25)
        print('\n' * 50), print('     ' * target_right , ' \  / '), print('     ' * target_right , '  \/  '), print('     ' * target_right , '  /\  '), print('     ' * target_right , ' /  \ ')
        t = 0
        while t < target_forward:
            print(' ')
            t += 1
        input ('The treasure can be found at this point     Tip: you could place your mouse at that place     Press enter to continue ')
        print('\n' * 50)
        b = 0
        times_right = 1
        times_forward = 1
        print('\n' * 50), print('     ' * target_right , ' \  / '), print('     ' * target_right , '  \/  '), print('     ' * target_right , '  /\  '), print('     ' * target_right , ' /  \ ')
        t = 0
        while t < times_forward:
            print(' ')
            t += 1
        while b < 500:
                direction = input (' which direction do you want to move in? use WASD keys to navigate')
                if direction == 'w':
                    times_forward += 1
                    print('\n' * 50), print('     ' * target_right , ' \  / '), print('     ' * target_right , '  \/  '), print('     ' * target_right , '  /\  '), print('     ' * target_right , ' /  \ ')
                    t = 0
                    while t < times_forward:
                        print(' ')
                        t += 1
                elif direction ==  'd':
                    times_right += 1
                    print('\n' * 50), print('     ' * target_right , ' \  / '), print('     ' * target_right , '  \/  '), print('     ' * target_right , '  /\  '), print('     ' * target_right , ' /  \ ')
                    t = 0
                    while t < times_forward:
                        print(' ')
                        t += 1
                elif direction ==  'a':
                    times_right -= 1
                    print('\n' * 50), print('     ' * target_right , ' \  / '), print('     ' * target_right , '  \/  '), print('     ' * target_right , '  /\  '), print('     ' * target_right , ' /  \ ')
                    t = 0
                    while t < times_forward:
                        print(' ')
                        t += 1
                elif direction ==  's':
                    times_forward -= 1
                    print('\n' * 50), print('     ' * target_right , ' \  / '), print('     ' * target_right , '  \/  '), print('     ' * target_right , '  /\  '), print('     ' * target_right , ' /  \ ')
                    t = 0
                    while t < times_forward:
                        print(' ')
                        t += 1
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
                        print('     ' * times_right , '  (o)  Yay!!!   I found a treasure'), print('     ' * times_right , '  \|/|---| '), print('     ' * times_right , '   | |---| '), print('     ' * times_right , '  / \ ')
                        t = 0
                        while t < times_forward:
                            print(' ')
                            t += 1
                        print('you have found the treasure')
                        print('good job')
                        break
        print('good job')
choice = ''
while choice != 'q':
    clearscreen()
    print('Welcome to Python Arcade')
    print('Games:')
    print('- Pong')
    print('- Flappy bird')
    print('- Crossy road')
    print('- Dino game')
    print('- Snake game')
    print('- Treasure hunt')
    print('- Number guessing')
    print('Type the first letter of the game you want to enter or press q to quit.')
    choice = input('Type your choice followed by enter: ')
    choice = choice.lower()
    if choice == 'p':
        #run pong
        clearscreen()
        movedirection = 'right'
        autoplay = False
        print('Pong')
        print('How to play: press contol + c to move your paddle up')
        name = input('enter your name ')
        if name == 'autoplay':
            autoplay, name = True, 'Autoplay Computer'
        pos = 49
        angle = 2
        score = 0
        waittime = 0.1
        padpos = 8
        pos = 8
        apos = 8
        p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18 = '','','','','','','','|','|','|','|','','','','','','',''
        s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = ' ',' ',' ',' ',' ',' ',' ','|','|','|','|',' ',' ',' ',' ',' ',' ',' '
        line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = ' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,((' '*50)+'o'+(' '*49)),' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100
        printarena(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
        lost = 10
        while True:
            try:
                time.sleep(waittime)
                line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = moveball(movedirection,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
                printarena(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18)
                if ((pos >= 98 and angle > 2) or pos >= 98) and lost > 9:
                    ln = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
                    if (ln == 1 and '|' in p1) or (ln == 2 and '|' in p2) or (ln == 3 and '|' in p3) or (ln == 4 and '|' in p4) or (ln == 5 and '|' in p5) or (ln == 6 and '|' in p6) or (ln == 7 and '|' in p7) or (ln == 8 and '|' in p8) or (ln == 9 and '|' in p9) or (ln == 10 and '|' in p10) or (ln == 11 and '|' in p11) or (ln == 12 and '|' in p12) or (ln == 13 and '|' in p13) or (ln == 14 and '|' in p14) or (ln == 15 and '|' in p15) or (ln == 16 and '|' in p16) or (ln == 17 and '|' in p17) or (ln == 18 and '|' in p18):
                        rand = randint(1,7)
                        if rand == 1 or rand == 2 or rand == 3:
                            movedirection = 'leftup'
                            angle = randint(2,4)
                        elif rand == 4 or rand == 5 or rand == 6:
                            movedirection = 'leftdown'
                            angle = randint(2,4)
                        else:
                            movedirection = 'left'
                            angle = 3
                    elif autoplay == False:
                        lost = 0
                    score += 1
                    if pos <= 3:
                        rand = randint(1,5)
                    if rand == 1 or rand == 2 or rand == 3:
                        movedirection = 'rightup'
                        angle = randint(2,4)
                    elif rand == 4 or rand == 5 or rand == 6:
                        movedirection = 'rightdown'
                        angle = randint(2,4)
                    else:
                        movedirection = 'right'
                        angle = 3
                if 'o' in line1:
                    if movedirection == 'leftdown':
                        movedirection = 'leftup'
                    else:
                        movedirection = 'rightup'
                if 'o' in line18:
                    if movedirection == 'leftup':
                        movedirection = 'leftdown'
                    else:
                        movedirection = 'rightdown'
                lost += 1
                if lost == 2:
                    print('you have lost')
                    break
                linein = 1 if ('o' in line1 ) else (1 if ('o' in line2 ) else (2 if ('o' in line3 ) else (2 if ('o' in line4 ) else (3 if ('o' in line5 ) else (4 if ('o' in line6 ) else (5 if ('o' in line7 ) else (6 if ('o' in line8 ) else (7 if ('o' in line9 ) else (8 if ('o' in line10 ) else (9 if ('o' in line11 ) else (10 if ('o' in line12 ) else (11 if ('o' in line13 ) else (12 if ('o' in line14 ) else (13 if ('o' in line15 ) else (14 if ('o' in line16 ) else (15 if ('o' in line17 ) else 16))))))))))))))))
                padstorer = padpos
                padpos = round(padpos)
                if ((pos <= 40 and angle >= 3) or (pos <= 25 and angle == 2) or pos <= 20) and (movedirection == 'left' or movedirection == 'leftup' or movedirection == 'leftdown'):
                    if spos > linein:
                        spos -= 1
                    if spos <= linein and spos <= 13:
                        spos += 1   
                    s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15,s16,s17,s18 = '|' if spos == 1 else ' ','|' if spos == 1 or spos == 2 else ' ','|' if spos == 1 or spos == 2 or spos == 3 else ' ','|' if spos == 1 or spos == 2 or spos == 3 or spos == 4 else ' ','|' if spos == 2 or spos == 3 or spos == 4 or spos == 5 else ' ','|' if spos == 3 or spos == 4 or spos == 5 or spos == 6 else ' ','|' if spos == 4 or spos == 5 or spos == 6 or spos == 7 else ' ','|' if spos == 5 or spos == 6 or spos == 7 or spos == 8 else ' ','|' if spos == 6 or spos == 7 or spos == 8 or spos == 9 else ' ','|' if spos == 7 or spos == 8 or spos == 9 or spos == 10 else ' ','|' if spos == 8 or spos == 9 or spos == 10 or spos == 11 else ' ','|' if spos == 9 or spos == 10 or spos == 11 or spos == 12 else ' ','|' if spos == 10 or spos == 11 or spos == 12 or spos == 12 else ' ','|' if spos == 11 or spos == 12 or spos == 13 or spos == 14 else ' ','|' if spos == 12 or spos == 13 or spos == 14 or spos == 15 else ' ','|' if spos == 13 or spos == 14 or spos == 15 or spos == 16 else ' ','|' if spos == 14 or spos == 15 or spos == 16 or spos == 17 else ' ','|' if spos == 15 or spos == 16 or spos == 17 or spos == 18 else ' '
                if (((pos >= 60 and angle >= 3) or (pos >= 75 and angle == 2) or pos >= 85) and (movedirection == 'right' or movedirection == 'rightup' or movedirection == 'rightdown')) and autoplay == True:
                    if apos > linein:
                        apos -= 1
                    if apos <= linein and apos <= 13:
                        apos += 1
                    padpos = apos
                p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18 = '|' if padpos == 1  or padpos == 2 else '','|' if padpos == 1 or padpos == 2 or padpos == 3 else '','|' if padpos == 1 or padpos == 2 or padpos == 3  or padpos == 4 else '','|' if padpos == 1 or padpos == 2 or padpos == 3 or padpos == 4 or padpos == 5 else '','|' if padpos == 2 or padpos == 3 or padpos == 4 or padpos == 5 or padpos == 6 else '','|' if padpos == 3 or padpos == 4 or padpos == 5 or padpos == 6  or padpos == 7 else '','|' if padpos == 4 or padpos == 5 or padpos == 6 or padpos == 7  or padpos == 8 else '','|' if padpos == 5 or padpos == 6 or padpos == 7 or padpos == 8  or padpos == 9 else '','|' if padpos == 6 or padpos == 7 or padpos == 8 or padpos == 9  or padpos == 10 else '','|' if padpos == 7 or padpos == 8 or padpos == 9 or padpos == 10  or padpos == 11 else '','|' if padpos == 8 or padpos == 9 or padpos == 10 or padpos == 11 or padpos == 12 else '','|' if padpos == 9 or padpos == 10 or padpos == 11 or padpos == 12  or padpos == 13 else '','|' if padpos == 10 or padpos == 11 or padpos == 12 or padpos == 13 or padpos == 14 else '','|' if padpos == 11 or padpos == 12 or padpos == 13 or padpos == 14 or padpos == 15 else '','|' if padpos == 12 or padpos == 13 or padpos == 14 or padpos == 15  or padpos == 16 else '','|' if padpos == 13 or padpos == 14 or padpos == 15 or padpos == 16  or padpos == 17 else '','|' if padpos == 14 or padpos == 15 or padpos == 16 or padpos == 17  or padpos == 18 else '','|' if padpos == 14 or padpos == 15 or padpos == 16 or padpos == 17 or padpos == 18 else ''
                print('Score: ',score,'    ',movedirection)
                if padpos > 1 and autoplay == False:
                    padpos = padstorer
                    padpos -= 0.3
            except:
                if padpos <= 13 and autoplay == False:
                    padpos += 2
            finally:
                blank = ''
        print('your score was ',score)
        input('press enter to continue')
    if choice == 'f':
        choice = ''
        held = False
        while choice != 'q':
            clearscreen()
            name = input('Enter your name: ')
            height = 10
            mover = 'up'
            lines = ' -'*50
            try:
                while True:
                    print('-'*100), print('\n'*(18-height)), print('(0)>'), print('\n'*height)
                    if mover == 'up':
                        height +=1
                    else:
                        height -= 1
                    if height >= 12:
                        mover = 'down'
                    if height <= 9:
                        mover = 'up'
                    print('press control c to start')
                    time.sleep(0.1)
            except:
                blank = ''
            adder = 0
            counter = 0
            height = 10
            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = '                  ','                  ','                  ','                  ','                  ','                  ','                  ','                  ','                  ','                  ','                  ','                  ','                  ','                  ','                  ','                  ','                  ','                  '
            count = 0
            score = 0
            linecontent = ''
            while True:
                try:
                    obstacleabove = ''
                    linein = int(round(height))
                    top = '\n' + obstacleabove
                    print(lines)
                    print(line18[1:100]),print(line17[1:100]),print(line16[1:100]),print(line15[1:100]),print(line14[1:100]),print(line13[1:100]),print(line12[1:100]),print(line11[1:100]),print(line10[1:100]),print(line9[1:100]),print(line8[1:100]),print(line7[1:100]),print(line6[1:100]),print(line5[1:100]),print(line4[1:100]),print(line3[1:100]),print(line2[1:100]),print(line1[1:100])
                    linecontent = line1 if linein == 1 else (line2 if linein == 2 else (line3 if linein == 3 else (line4 if linein == 4 else (line5 if linein == 5 else (line6 if linein == 6 else (line7 if linein == 7 else (line8 if linein == 8 else (line9 if linein == 9 else (line10 if linein == 10 else (line11 if linein == 11 else (line12 if linein == 12 else (line12 if linein == 12 else (line13 if linein == 13 else (line14 if linein == 14 else (line15 if linein == 15 else (line16 if linein == 16 else (line17 if linein == 17 else line18)))))))))))))))))
                    linecontentshow = linecontent
                    linein += 1
                    linecontentabove = line1 if linein == 1 else (line2 if linein == 2 else (line3 if linein == 3 else (line4 if linein == 4 else (line5 if linein == 5 else (line6 if linein == 6 else (line7 if linein == 7 else (line8 if linein == 8 else (line9 if linein == 9 else (line10 if linein == 10 else (line11 if linein == 11 else (line12 if linein == 12 else (line12 if linein == 12 else (line13 if linein == 13 else (line14 if linein == 14 else (line15 if linein == 15 else (line16 if linein == 16 else (line17 if linein == 17 else (line18 if linein == 18 else (''*100)))))))))))))))))))
                    linein -= 2
                    linecontentbelow = line1 if linein == 1 else (line2 if linein == 2 else (line3 if linein == 3 else (line4 if linein == 4 else (line5 if linein == 5 else (line6 if linein == 6 else (line7 if linein == 7 else (line8 if linein == 8 else (line9 if linein == 9 else (line10 if linein == 10 else (line11 if linein == 11 else (line12 if linein == 12 else (line12 if linein == 12 else (line13 if linein == 13 else (line14 if linein == 14 else (line15 if linein == 15 else (line16 if linein == 16 else (line17 if linein == 17 else (line18 if linein == 18 else (''*100)))))))))))))))))))
                    linein += 1
                    try:
                        if linecontent[2] == '|' :
                            print('\n'+('_'*100))
                            print('you have crashed')
                            print('linecontent[2] was line')
                            break
                        if linecontent[3] == '|' :
                            print('\n'+('_'*100))
                            print('you have crashed')
                            print('linecontent[3] was line')
                            break
                        if linecontent[4] == '|' :
                            print('\n'+('_'*100))
                            print('you have crashed')
                            print('linecontent[4] was line')
                            break
                    except:
                        blank = ''
                    height -= 0.5
                    print(lines)
                    print('Score: ',score,'     Player: ',name)
                    time.sleep(0.1)
                    count += 1
                    score += 1
                    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('(0)>','    '), line2.replace('(0)>','    '),line3.replace('(0)>','    '),line4.replace('(0)>','    '),line5.replace('(0)>','    '),line6.replace('(0)>','    '),line7.replace('(0)>','    '),line8.replace('(0)>','    '),line9.replace('(0)>','    '),line10.replace('(0)>','    '),line11.replace('(0)>','    '),line12.replace('(0)>','    '),line13.replace('(0)>','    '),line14.replace('(0)>','    '),line15.replace('(0)>','    '),line16.replace('(0)>','    '),line17.replace('(0)>','    '),line18.replace('(0)>','    ')
                    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1[1:],line2[1:],line3[1:],line4[1:],line5[1:],line6[1:],line7[1:],line8[1:],line9[1:],line10[1:],line11[1:],line12[1:],line13[1:],line14[1:],line15[1:],line16[1:],line17[1:],line18[1:]
                    bird = '(0)>'
                    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addbird(line1) if int(round(height,0)) == 1 else line1),(addbird(line2) if int(round(height,0)) == 2 else line2),(addbird(line3) if int(round(height,0)) == 3 else line3),(addbird(line4) if int(round(height,0)) == 4 else line4),(addbird(line5) if int(round(height,0)) == 5 else line5),(addbird(line6) if int(round(height,0)) == 6 else line6),(addbird(line7) if int(round(height,0)) == 7 else line7),(addbird(line8) if int(round(height,0)) == 8 else line8),(addbird(line9) if int(round(height,0)) == 9 else line9),(addbird(line10) if int(round(height,0)) == 10 else line10),(addbird(line11) if int(round(height,0)) == 11 else line11),(addbird(line12) if int(round(height,0)) == 12 else line12),(addbird(line13) if int(round(height,0)) == 13 else line13),(addbird(line14) if int(round(height,0)) == 14 else line14),(addbird(line15) if int(round(height,0)) == 15 else line15),(addbird(line16) if int(round(height,0)) == 16 else line16),(addbird(line17) if int(round(height,0)) == 17 else line17),(addbird(line18) if int(round(height,0)) == 18 else line18)
                    lines = lines[1:]
                    lines = (lines + ' ') if lines[-1] == '-' else (lines + '-')
                    if height <= 0:
                        print('you have hit the ground')
                        break
                    if height >= 18.5:
                        print('you have hit the ceiling')
                        break
                    if counter == 10:
                        counter = 0
                        regspace = '                          '
                        addline =  '                         |'
                        rand = randint(1,15)
                        if rand == 1:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+regspace,line2+regspace,line3+regspace,line4+regspace,line5+regspace,line6+addline,line7+addline,line8+addline,line9+addline,line10+addline,line11+addline,line12+addline,line13+addline,line14+addline,line15+addline,line16+addline,line17+addline,line18+addline
                        elif rand == 2:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+regspace,line3+regspace,line4+regspace,line5+regspace,line6+addline,line7+addline,line8+addline,line9+addline,line10+addline,line11+addline,line12+addline,line13+addline,line14+addline,line15+addline,line16+addline,line17+addline,line18+addline
                        elif rand == 3:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+regspace,line4+regspace,line5+regspace,line6+regspace,line7+addline,line8+addline,line9+addline,line10+addline,line11+addline,line12+addline,line13+addline,line14+addline,line15+addline,line16+addline,line17+addline,line18+addline
                        elif rand == 4:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+addline,line4+regspace,line5+regspace,line6+regspace,line7+regspace,line8+addline,line9+addline,line10+addline,line11+addline,line12+addline,line13+addline,line14+addline,line15+addline,line16+addline,line17+addline,line18+addline
                        elif rand == 5:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+addline,line4+addline,line5+regspace,line6+regspace,line7+regspace,line8+regspace,line9+addline,line10+addline,line11+addline,line12+addline,line13+addline,line14+addline,line15+addline,line16+addline,line17+addline,line18+addline
                        elif rand == 6:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+addline,line4+addline,line5+addline,line6+regspace,line7+regspace,line8+regspace,line9+regspace,line10+addline,line11+addline,line12+addline,line13+addline,line14+addline,line15+addline,line16+addline,line17+addline,line18+addline
                        elif rand == 7:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+addline,line4+addline,line5+addline,line6+addline,line7+regspace,line8+regspace,line9+regspace,line10+regspace,line11+addline,line12+addline,line13+addline,line14+addline,line15+addline,line16+addline,line17+addline,line18+addline
                        elif rand == 8:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+addline,line4+addline,line5+addline,line6+addline,line7+addline,line8+regspace,line9+regspace,line10+regspace,line11+regspace,line12+addline,line13+addline,line14+addline,line15+addline,line16+addline,line17+addline,line18+addline
                        elif rand == 9:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+addline,line4+addline,line5+addline,line6+addline,line7+addline,line8+addline,line9+regspace,line10+regspace,line11+regspace,line12+regspace,line13+addline,line14+addline,line15+addline,line16+addline,line17+addline,line18+addline
                        elif rand == 10:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+addline,line4+addline,line5+addline,line6+addline,line7+addline,line8+addline,line9+addline,line10+regspace,line11+regspace,line12+regspace,line13+regspace,line14+addline,line15+addline,line16+addline,line17+addline,line18+addline
                        elif rand == 11:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+addline,line4+addline,line5+addline,line6+addline,line7+addline,line8+addline,line9+addline,line10+addline,line11+regspace,line12+regspace,line13+regspace,line14+regspace,line15+addline,line16+addline,line17+addline,line18+addline
                        elif rand == 12:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+addline,line4+addline,line5+addline,line6+addline,line7+addline,line8+addline,line9+addline,line10+addline,line11+addline,line12+regspace,line13+regspace,line14+regspace,line15+regspace,line16+addline,line17+addline,line18+addline
                        elif rand == 13:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+addline,line4+addline,line5+addline,line6+addline,line7+addline,line8+addline,line9+addline,line10+addline,line11+addline,line12+addline,line13+regspace,line14+regspace,line15+regspace,line16+regspace,line17+addline,line18+addline
                        elif rand == 14:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+addline,line4+addline,line5+addline,line6+addline,line7+addline,line8+addline,line9+addline,line10+addline,line11+addline,line12+addline,line13+addline,line14+regspace,line15+regspace,line16+regspace,line17+regspace,line18+addline
                        else:
                            line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1+addline,line2+addline,line3+addline,line4+addline,line5+addline,line6+addline,line7+addline,line8+addline,line9+addline,line10+addline,line11+addline,line12+addline,line13+addline,line14+addline,line15+regspace,line16+regspace,line17+regspace,line18+regspace
                    counter += 1
                except:
                    height += 2
                    time.sleep(0.2)
            appended = False
            while True:
                try:
                    print('you have lost')
                    print('your score was ', score)
                    print(' image of crash below'),print(linecontentabove[:100]),print(linecontentshow[:100]),print(linecontentbelow[:100])
                    toadd = name + (' '*(20-len(name))) + str(score) + '\n'
                    try:
                        read = shelveread('flappybirdscores')
                    except:
                        read = ''
                    try:
                        highscore = int(shelveread('flappyhighscore'))
                    except:
                        highscore = shelvewrite('flappyhighscore','0')
                        highscore = 0
                    if appended == False:
                        try:
                            shelveappend('flappybirdscores', toadd)
                        except:
                            shelvewrite('flappybirdscores', toadd)
                        try:
                            if score >= highscore:
                                print('you have made a new highscore')
                                highscore = score
                            shelvewrite('flappyhighscore',str(highscore))
                        except:
                            blank = ''
                        appended = True
                    print('\n\n Scoreboard: ')
                    print('_________________')
                    print('Highscore' + (' '*(20-len(str(highscore)))) + str(highscore))
                    print('_________________')
                    print(shelveread('flappybirdscores'))
                    print('Press enter to return to the main menu. Press q and enter to quit  ')
                    choice = input('you can also enter an override command like scoreboard.clear or scoreboard.dontsave\n')
                    if choice == 'scoreboard.clear':
                        shelvewrite('flappybirdscores', '')
                        print('scoreboard shown below. press enter to continue')
                        print(shelveread('flappybirdscores'))
                    if choice == 'scoreboard.dontsave':
                        shelvewrite('flappybirdscores',read)
                        print('scoreboard shown below. press enter to continue')
                        print(shelveread('flappybirdscores'))
                    break
                except:
                    blank = '' 
        input('press enter to continue')
    if choice == 'c':
        choice = ''
        skipped = 'yep'
        while choice != 'q':
            clearscreen()
            print('Crossy Road'), print('___________\n\n'), print('How to play'), print(' 1. Press control+c to move foreward'), print(' 2. When you hit an obstacle the game will end\n\n'), print(' Select a level or type s for scoreboard\n'), print(' Easy * Medium * Hard * Very hard * Xpert * Scoreboard')
            level = input('\n Type the first letter of your choice ')
            level = level.lower()
            if 's' in level:
                print(shelveread('crossyrdscores'))
                input('press enter to continue'), clearscreen()
                print('Crossy Road'), print('___________\n\n'), print('How to play'), print(' 1. Press control+c to move foreward'), print(' 2. When you hit an obstacle the game will end\n\n'), print(' Select a level\n'), print(' Easy * Medium * Hard * Very hard * Xpert')
                level = input('\n Type the first letter of your choice ')
                level = level.lower()
            level = 'Easy' if 'e' in level else ('Medium' if 'm' in level else ('Hard' if 'h' in level else ('Very hard' if 'v' in level else ('Xpert' if 'x' in level else 'Easy'))))
            level = level.lower()
            waittime = 0.33 if 'easy' in level else (0.25 if 'medium' in level else (0.2 if 'hard' in level else (0.15 if 'very hard' in level else (0.12))))
            clearscreen(), print('Crossy Road')
            print('___________\n\n'), print('How to play'), print(' 1. Press control+c to move foreward'), print(' 2. When you hit an obstacle the game will end\n\n'), print(' Level: ', level), print(' \n')
            name = input('Enter your name ')
            print(12 * ('\n\n'+('-'*125)))
            inlane = 0
            score = 110
            one = True
            lost = False
            spaces = str(' '*125)
            counter = 0
            lanerender = 0
            b1,b2,b3, first = str(' '*65), str(' '*65), str(' '*65), str(' '*65 + '(--)') 
            lane1, lane2, lane3, lane4, lane5, lane6 =  spaces, spaces, spaces, spaces, spaces, spaces
            printlanes(lane1,lane2,lane3,'','','','')
            #randomly generating part ahead
            while True:
                try:
                    randomizer = randint(1,6)
                    rand = randint(1,14)
                    rand0 = '=' if rand == 1 else ('?' if rand == 2 else ('$' if rand == 3 else ('<>' if rand == 4 else ('|' if rand == 5 else ('-' if rand == 6 else ('+' if rand == 7 else ('W' if rand == 8 else ('<' if rand == 9 else ('~' if rand == 10 else ('{' if rand == 11 else ('[' if rand == 12 else ('!' if rand == 13 else 'K'))))))))))))
                    rand = randint(1,14)
                    rand1 = '=' if rand == 1 else ('?' if rand == 2 else ('$' if rand == 3 else ('<>' if rand == 4 else ('|' if rand == 5 else ('----' if rand == 6 else ('=+=' if rand == 7 else ('W' if rand == 8 else ('<->' if rand == 9 else ('~~' if rand == 10 else ('{' if rand == 11 else ('[' if rand == 12 else ('!' if rand == 13 else 'K--'))))))))))))
                    rand = randint(1,14)
                    rand2 = '==' if rand == 1 else ('¿?' if rand == 2 else ('$$$' if rand == 3 else ('<->' if rand == 4 else ('/|' if rand == 5 else ('-_-_-' if rand == 6 else ('=++=' if rand == 7 else ('WV' if rand == 8 else ('<_>' if rand == 9 else ('~-~' if rand == 10 else ('{}' if rand == 11 else ('[]' if rand == 12 else ('¡!' if rand == 13 else '-K-'))))))))))))
                    add1,add2,add3,add4,add5 = ' ',' ',' ',' ',' '
                    if randomizer == 1:
                        add1 = rand0
                        add2 = rand0
                        if waittime == 0.2:
                            add3 = rand1
                            if waittime == 0.12:
                                add4 = rand2
                    if randomizer == 2:
                        add2 = rand1
                        add3 = rand0
                        if waittime == 0.15:
                            add4 = rand1
                    if randomizer == 3:
                        add3 = rand0
                        add4 = rand0
                        if waittime == 0.12:
                            add1 = rand2
                    lane1, lane2, lane3 = refreshlanecontent(add1,lane1), refreshlanecontent(add2,lane2), refreshlanecontent(add3,lane3)
                    if counter >= 60:
                        if lanerender == 0:
                            printlanes(lane1, b1, lane2, b2, lane3, b3, first)
                        elif lanerender == 1:
                            printlanes(lane1, b1, lane2, b2, lane3, b3,'')
                        elif lanerender == 'b1':
                            printlanes(b1, lane2, b2, lane3, b3, lane1, '')
                        elif lanerender == 2:
                            printlanes(lane2, b2, lane3, b3, lane1, b1, '')
                        elif lanerender == 'b2':
                            printlanes(b2, lane3, b3, lane1, b1, lane2, '')
                        elif lanerender == 3:
                            printlanes(lane3, b3, lane1, b1, lane2, b2, '')
                        elif lanerender == 'b3':
                            printlanes(b3, lane1, b1, lane2, b2, lane3, '')
                        print('Score: ', score,'   lanerender: ', lanerender)
                        time.sleep(waittime)
                    if score <= 0:
                        lost == True
                        print('You have run out of time')
                        break
                    if lost == True:
                        break
                    counter += 1
                    score -= 1
                except(KeyboardInterrupt, SystemExit):
                    if skipped == 'nope':
                        input('you jumped too many times')
                        break
                    skipped = 'nope'
                    if inlane == 0:
                        inlane += 1
                        lanerender = 1
                        b3 = removeguyfromlane(b3)
                        lane1 = addguytolanecontent(lane1)
                    elif inlane == 1:
                        lanerender = 'b1'
                        inlane += 1
                        lane1 = removeguyfromlane(lane1)
                        b1 = addguytolanecontent(b1)
                    elif inlane == 2:
                        lanerender = 2
                        inlane += 1
                        b1 = removeguyfromlane(b1)
                        lane2 = addguytolanecontent(lane2)
                    elif inlane == 3:
                        lanerender = 'b2'
                        inlane += 1
                        lane2 = removeguyfromlane(lane2)
                        b2 = addguytolanecontent(b2)
                    elif inlane == 4:
                        lanerender = 3
                        inlane += 1
                        b2 = removeguyfromlane(b2)
                        lane3 = addguytolanecontent(lane3)
                    elif inlane == 5:
                        lanerender = 'b3'
                        lane3 = removeguyfromlane(lane3)
                        b3 = addguytolanecontent(b3)
                        inlane += 1
                    elif inlane == 6:
                        lanerender = 0
                        inlane = 0
                    score += 100
                    skipped = 'yep'
            appended = False
            while True:
                try:
                    clearscreen()
                    print('you have lost')
                    print('your score was ', round(score,0))
                    readbefore = shelveread('crossyrdscores')
                    toadd = name + (' '*(20-len(name))) + str(score) + '\n'
                    if appended == False:
                        try:
                            shelveappend('crossyrdscores', toadd)
                        except:
                            shelvewrite('crossyrdscores', toadd)
                        appended = True
                    print('\n\n Scoreboard: ')
                    print(shelveread('crossyrdscores'))
                    print('Press enter to return to the main menu. Press q and enter to quit  ')
                    choice = input('you can also enter an override command like scoreboard.clear or scoreboard.dontsave\n')
                    if choice == 'scoreboard.clear':
                        shelvewrite('crossyrdscores', '')
                        print('scoreboard shown below. press enter to continue')
                        print(shelveread('crossyrdscores'))
                        input()
                    if choice == 'scoreboard.dontsave':
                        shelvewrite('crossyrdscores', readbefore)
                        print('scoreboard shown below. press enter to continue')
                        print(shelveread('crossyrdscores'))
                        input()
                    break
                except:
                    blank = ''
        input('press enter to continue')
    if choice == 'd':
        spaces = 65
        spaces1 = 45
        score = 0
        successjump = 0
        failjump = 0
        high = 0000
        speed = 0.07
        newscore = False
        name = input('Enter your name ')
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
                score = str(score)
                toprint = 'score: ' + score + '\n                     YOU' + (firstspaces * ' ')+ first_obj +(secondspaces * ' ')+ second_obj
                score = int(score)
                print(toprint[:110])
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
        input('press enter to continue')
    if choice == 's':
        clearscreen()
        autoplay = False
        name = input('enter your name: ')
        if name == 'autoplay':
            autoplay = True
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
                printarenasnake()
                ln = height #ln = 1 if ('o' in l1 ) else (2 if ('o' in l2 ) else (3 if ('o' in l3 ) else (4 if ('o' in l4 ) else (5 if ('o' in l5 ) else (6 if ('o' in l6 ) else (7 if ('o' in l7 ) else (8 if ('o' in l8 ) else (9 if ('o' in l9 ) else (10 if ('o' in l10 ) else (11 if ('o' in l11 ) else (12 if ('o' in l12 ) else (13 if ('o' in l13 ) else (14 if ('o' in l14 ) else (15 if ('o' in l15 ) else (16 if ('o' in l16 ) else (17 if ('o' in l17 ) else 18))))))))))))))))
                if turningmode == True:
                    blank = ''
                    #turn
                else:
                    ln = height
                    #ln = 1 if ('o' in l1 ) else (2 if ('o' in l2 ) else (3 if ('o' in l3 ) else (4 if ('o' in l4 ) else (5 if ('o' in l5 ) else (6 if ('o' in l6 ) else (7 if ('o' in l7 ) else (8 if ('o' in l8 ) else (9 if ('o' in l9 ) else (10 if ('o' in l10 ) else (11 if ('o' in l11 ) else (12 if ('o' in l12 ) else (13 if ('o' in l13 ) else (14 if ('o' in l14 ) else (15 if ('o' in l15 ) else (16 if ('o' in l16 ) else (17 if ('o' in l17 ) else 18))))))))))))))))
                    if direction == 'right':
                        removeballsnake()
                        pos = pos + 1
                        l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = (addballsnake(l1) if ln == 1 else l1),(addballsnake(l2) if ln == 2 else l2),(addballsnake(l3) if ln == 3 else l3),(addballsnake(l4) if ln == 4 else l4),(addballsnake(l5) if ln == 5 else l5),(addballsnake(l6) if ln == 6 else l6),(addballsnake(l7) if ln == 7 else l7),(addballsnake(l8) if ln == 8 else l8),(addballsnake(l9) if ln == 9 else l9),(addballsnake(l10) if ln == 10 else l10),(addballsnake(l11) if ln == 11 else l11),(addballsnake(l12) if ln == 12 else l12),(addballsnake(l13) if ln == 13 else l13),(addballsnake(l14) if ln == 14 else l14),(addballsnake(l15) if ln == 15 else l15),(addballsnake(l16) if ln == 16 else l16),(addballsnake(l17) if ln == 17 else l17),(addballsnake(l18) if ln == 18 else l18)
                    if direction == 'left':
                        removeballsnake()
                        pos = pos - 1
                        l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18 = (addballsnake(l1) if ln == 1 else l1),(addballsnake(l2) if ln == 2 else l2),(addballsnake(l3) if ln == 3 else l3),(addballsnake(l4) if ln == 4 else l4),(addballsnake(l5) if ln == 5 else l5),(addballsnake(l6) if ln == 6 else l6),(addballsnake(l7) if ln == 7 else l7),(addballsnake(l8) if ln == 8 else l8),(addballsnake(l9) if ln == 9 else l9),(addballsnake(l10) if ln == 10 else l10),(addballsnake(l11) if ln == 11 else l11),(addballsnake(l12) if ln == 12 else l12),(addballsnake(l13) if ln == 13 else l13),(addballsnake(l14) if ln == 14 else l14),(addballsnake(l15) if ln == 15 else l15),(addballsnake(l16) if ln == 16 else l16),(addballsnake(l17) if ln == 17 else l17),(addballsnake(l18) if ln == 18 else l18)
                    if direction == 'up':
                        height += 1
                        removeballsnake()
                        l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l6,l17,l18 = (addballsnake(l2) if ln == 1 else l2),(addballsnake(l3) if ln == 2 else l3),(addballsnake(l4) if ln == 3 else l4),(addballsnake(l5) if ln == 4 else l5),(addballsnake(l6) if ln == 5 else l6),(addballsnake(l7) if ln == 6 else l7),(addballsnake(l8) if ln == 7 else l8),(addballsnake(l9) if ln == 8 else l9),(addballsnake(l10) if ln == 9 else l10),(addballsnake(l11) if ln == 10 else l11),(addballsnake(l12) if ln == 11 else l12),(addballsnake(l13) if ln == 12 else l13),(addballsnake(l14) if ln == 13 else l14),(addballsnake(l15) if ln == 14 else l15),(addballsnake(l16) if ln == 15 else l16),(addballsnake(l17) if ln == 16 else l17),(addballsnake(l18) if ln == 17 else l18)
                    if direction == 'down':
                        height -= 1
                        removeballsnake()
                        l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l6,l17 = (addballsnake(l1) if ln == 2 else l1),(addballsnake(l2) if ln == 3 else l2),(addballsnake(l3) if ln == 4 else l3),(addballsnake(l4) if ln == 5 else l4),(addballsnake(l5) if ln == 6 else l5),(addballsnake(l6) if ln == 7 else l6),(addballsnake(l7) if ln == 8 else l7),(addballsnake(l8) if ln == 9 else l8),(addballsnake(l9) if ln == 10 else l9),(addballsnake(l10) if ln == 11 else l10),(addballsnake(l11) if ln == 12 else l11),(addballsnake(l12) if ln == 13 else l12),(addballsnake(l13) if ln == 14 else l13),(addballsnake(l14) if ln == 15 else l14),(addballsnake(l15) if ln == 16 else l15),(addballsnake(l16) if ln == 17 else l16),(addballsnake(l17) if ln == 18 else l17)
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
                        if randheight < height:
                            direction = 'down'
                        else:
                            direction = 'up'
                    else:
                        if randpos <= pos:
                            direction = 'left'
                        else:
                            direction = 'right'
        print('you have lost')
        input('press enter to continue')
    if choice == 't':
        treasure_hunt()
        input('press enter to continue')
    if choice == 'n':
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
        input('press enter to continue')