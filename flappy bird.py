import time, shelve
from random import randint
def clearscreen():
    print('\n'*50)
def addbird(line):
    line = '(0)>' + line[4:]
    return line
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