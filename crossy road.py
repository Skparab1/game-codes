import time, random
from random import randint
def clearscreen(): 
    print('\n' * 50)
clearscreen()
print('Crossy Road')
print('___________\n\n')
print('How to play')
print(' 1. Press control+c to move foreward')
print(' 2. When you hit an obstacle the game will end\n\n')
name = input('enter your name ')
def printlanes(content1, content2, content3,b1,b2):
    global score
    print('-'*125,'\n\n'), print('-'*125,'\n\n'), print('-'*125),print(content3), print(content3),print('-'*125),print(b2),print(b2),print('-'*125),print(content2), print(content2), print('-'*125),print(b1),print(b1),print('-'*125),print(content1), print(content1), print('-'*125)
def refreshlanecontent(newcontent, lanecontent):
    global lost
    numtoadd = randint(0,2)
    lanecontent = str(lanecontent)
    dellanes = (-1 * numtoadd) - 1 
    savecontent = lanecontent[0:dellanes]
    lanecontent = (numtoadd * ' ') + newcontent + savecontent
    if '(' in lanecontent:
        if lanecontent[64] != ' ' or lanecontent[65] != ' ':
            lost = True
        lanecontent = removeguyfromlane(lanecontent)
        lanecontent = addguytolanecontent(lanecontent)
    return lanecontent
def removeguyfromlane(lanecontent):
    lane = lanecontent.replace('(--)','')
    return lane
def addguytolanecontent(lanecontent):
    firstpart = lanecontent[0:65]
    secondpart = lanecontent[65:]
    final = firstpart + '(--)' + secondpart
    return final
print(12 * ('\n\n'+('-'*125)))
inlane = 0
score = 50
one = True
lost = False
spaces = str(' '*125)
counter = 0
b1,b2,b3 = str(' '*65), str(' '*65), str(' '*65)
lane1, lane2, lane3, lane4, lane5, lane6 =  spaces, spaces, spaces, spaces, spaces, spaces
printlanes(lane1,lane2,lane3,'','')
#randomly generating part ahead
while True:
    try:
        randomizer = randint(1,6)
        rand = randint(1,14)
        rand = '=' if rand == 1 else ('?' if rand == 2 else ('$' if rand == 3 else ('<>' if rand == 4 else ('|' if rand == 5 else ('-' if rand == 6 else ('+' if rand == 7 else ('W' if rand == 8 else ('<' if rand == 9 else ('~' if rand == 10 else ('{' if rand == 11 else ('[' if rand == 12 else ('!' if rand == 13 else 'K'))))))))))))
        add1,add2,add3,add4,add5 = ' ',' ',' ',' ',' '
        if randomizer == 1:
            add1 = rand
            add2 = rand
        if randomizer == 2:
            add2 = rand
            add3 = rand
        if randomizer == 3:
            add3 = rand
            add4 = rand
        if randomizer == 4:
            add4 = rand
            add1 = rand
        lane1, lane2, lane3, lane4, lane5 = refreshlanecontent(add1,lane1), refreshlanecontent(add2,lane2), refreshlanecontent(add3,lane3), refreshlanecontent(add4,lane4), refreshlanecontent(add5,lane5)
        if counter >= 60:
            printlanes(lane1,lane2,lane3,b1,b2)
            if inlane == 0: 
                print(' ' * 65, ' (--)\n',' ' * 65,'(--)')
                print(score)
            else:
                print('Score')
                print(score)
            time.sleep(0.25)
        if score <= 0:
            lost == True
            print('You have run out of time')
        if lost == True:
            break
        counter += 1
        score += 1
    except(KeyboardInterrupt, SystemExit):
        #move foreward
        if inlane == 0:
            inlane += 1
            lane1 = addguytolanecontent(lane1)
        elif inlane == 1:
            inlane += 1
            lane1 = removeguyfromlane(lane1)
            b1 = addguytolanecontent(b1)
        elif inlane == 2:
            inlane += 1
            b1 = removeguyfromlane(b1)
            lane2 = addguytolanecontent(lane2)
        elif inlane == 3:
            inlane += 1
            lane2 = removeguyfromlane(lane2)
            b2 = addguytolanecontent(b2)
        elif inlane == 4:
            inlane += 1
            b2 = removeguyfromlane(b2)
            lane3 = addguytolanecontent(lane3)
        elif inlane == 5:
            inlane += 1
            lane3 = removeguyfromlane(lane3)
            b3 = addguytolanecontent(b3)
        elif inlane == 6:
            inlane += 1
            b3 = removeguyfromlane(b3)
            lane4 = addguytolanecontent(lane4)
        if inlane >= 6:
            lane4 = removeguyfromlane(lane4)
            inlane = 0
        score += 100
print('you have lost')
print('your score was ', round(score,0))
#highscore board