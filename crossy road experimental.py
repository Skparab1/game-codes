import time, random
from random import randint
import shelve
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
choice = ''
skipped = 'yep'
while choice != 'q':
    clearscreen()
    print('Crossy Road'), print('___________\n\n'), print('How to play'), print(' 1. Press control+c to move foreward'), print(' 2. When you hit an obstacle the game will end\n\n'), print(' Select a level\n'), print(' Easy * Medium * Hard * Very hard * Xpert')
    level = input('\n Type the first letter of your choice ')
    level = level.lower()
    level = 'Easy' if 'e' in level else ('Medium' if 'm' in level else ('Hard' if 'h' in level else ('Very hard' if 'v' in level else ('Xpert'))))
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
            print('you have lost')
            print('your score was ', round(score,0))
            toadd = name + (' '*(20-len(name))) + str(score) + '\n'
            if appended == False:
                try:
                    shelveappend('crossyrdscores', toadd)
                except:
                    shelvewrite('crossyrdscores', toadd)
                appended = True
            print('\n\n Scoreboard: ')
            print(shelveread('crossyrdscores'))
            choice = input('Press enter to return to the main menu. Press q and enter to quit  ')
            if choice == 'scoreboard.clear':
                shelvewrite('crossyrdscores', '')
            break
        except:
            blank = ''