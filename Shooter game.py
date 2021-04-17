import string
import time
pos = 50
#26 lines
l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15,l16,l17,l18,l19,l20,l21,l22,l23,l24,l25,l26 = '','','','','','','','','','','','','','','','','','','','',str(' '*50 + '='),'','','',str(' '*50 + '='),'' 
fish = 'r'
objdist = 20
shootdist = 1
shootspace = 0
balls = 50
def gameprocessor(onebefore,onetoprocess,nextone,secondone):
    if '=' in onetoprocess:
        onetoprocessbackup = onetoprocess
        nextonebackup = nextone
        secondonebackup = secondone
        onebefore = nextonebackup
        onetoprocess = secondonebackup
        nextone = onetoprocessbackup
        decider = True
    else:
        onebefore = onetoprocess
        decider = False
    return onebefore,onetoprocess,nextone,secondone,decider
while True:
    try:
        #obstacle/ball processor
        l26 = l25
        l25 = l24
        l24 = l23
        l23 = l22
        l22 = l21
        l21 = l20
        l20 = l19
        l19 = l18
        l18 = l17
        l17 = l16
        l16 = l15
        l15 = l14
        l14 = l13
        l13 = l12
        l12 = l11
        l11 = l10
        l10 = l9
        l9 = l8
        l8 = l7
        l7 = l6
        l6 = l5
        l5 = l4
        l4 = l3
        l3 = l2
        l2 = l1
        l1 = ''
        decide = False
        while decide == False:
            l25,l24,l23,l22,decide = gameprocessor(l25,l24,l23,l22)
            l24,l23,l22,l21,decide = gameprocessor(l24,l23,l22,l21)
            l23,l22,l21,l20,decide = gameprocessor(l23,l22,l21,l20)
            l22,l21,l20,l19,decide = gameprocessor(l22,l21,l20,l19)
            l21,l20,l19,l18,decide = gameprocessor(l21,l20,l19,l18)
            l20,l19,l18,l17,decide = gameprocessor(l20,l19,l18,l17)
            l19,l18,l17,l16,decide = gameprocessor(l19,l18,l17,l16)
            l18,l17,l16,l15,decide = gameprocessor(l18,l17,l16,l15)
            l17,l16,l15,l14,decide = gameprocessor(l17,l16,l15,l14)
            l16,l15,l14,l13,decide = gameprocessor(l16,l15,l14,l13)
            l15,l14,l13,l12,decide = gameprocessor(l15,l14,l13,l12)
            l14,l13,l12,l11,decide = gameprocessor(l14,l13,l12,l11)
            l13,l12,l11,l10,decide = gameprocessor(l13,l12,l11,l10)
            l12,l11,l10,l9,decide = gameprocessor(l12,l11,l10,l9)
            l11,l10,l9,l8,decide = gameprocessor(l11,l10,l9,l8)
            l10,l9,l8,l7,decide = gameprocessor(l10,l9,l8,l7)
            l9,l8,l7,l6,decide = gameprocessor(l9,l8,l7,l6)
            l8,l7,l6,l5,decide = gameprocessor(l8,l7,l6,l5)
            l7,l6,l5,l4,decide = gameprocessor(l7,l6,l5,l4)
            l6,l5,l4,l3,decide = gameprocessor(l6,l5,l4,l3)
            l5,l4,l3,l2,decide = gameprocessor(l5,l4,l3,l2)
            l4,l3,l2,l1,decide = gameprocessor(l4,l3,l2,l1)
        print(l26,'\n',l25,'\n',l24,'\n',l23,'\n',l22,'\n',l21,'\n',l20,'\n',l19,'\n',l18,'\n',l17,'\n',l16,'\n',l15,'\n',l14,'\n',l13,'\n',l12,'\n',l11,'\n',l10,'\n',l9,'\n',l8,'\n',l7,'\n',l6,'\n',l5,'\n',l4,'\n',l3,'\n',l2,'\n',l1)
        print
        if balls <= 0:
            break
        print('balls: ',balls)
        print(' '*pos,' ||')
        print(' '*pos,' ||')
        print(' '*pos,'<||>')
        print(' '*pos,'<__>')
        if pos == 44 or pos == 46 or pos == 48 or pos == 50 or pos == 52 or pos == 54 or pos == 56:
            pos += 2
        if pos == 58:
            pos -= 1
        if pos == 43:
            pos += 1
        if pos == 57 or pos == 55 or pos == 53 or pos == 51 or pos == 49 or pos == 47 or pos == 45:
            pos -= 2
        objdist -= 1
        time.sleep(1)
        print('\n'*30)
    except(KeyboardInterrupt,SystemExit):
        print('\n'*30)
        balls -= 1
        l1 = pos*' '+'o'
print('GAME OVER       YOU ARE OUT OF BALLS')