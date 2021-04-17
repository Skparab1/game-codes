spaces = -20
first_item = 'item'
spaces2 = 0
spaces3 = -40
score = 1
item1 = ''
item2 = ''
item3 = ''
time1 = 0
from random import randint
import time
import socket
def return_item():
    randomnum = randint(1,8)
    if randomnum == 1:
        item = 'carrot'
    elif randomnum == 2:
        item = 'fishy'
    elif randomnum == 3:
        item = 'eggy'
    elif randomnum == 4:
        item = 'doggy'
    elif randomnum == 5:
        item = 'trash'
    elif randomnum == 6:
        item = 'catty'
    elif randomnum == 7:
        item = 'bread'
    else:
        item = 'bunny'
    return item
item = return_item()
item2 = return_item()
item3 = return_item()
while True:
    try:
        spacer2 = 0
        print('\n'*50)
        print('                 doggy              carrot     bunny          catty              fishy         eggy          trash               \ ')
        print(' '*spaces, item)
        print(' '*spaces2, item2)
        print(' '*spaces3, item3)
        print('_____________             ________                     _____          ________             __        _____            _____       \ ')
        print('             \           /        \        /\         /     \        /        \           /  \      /     \          /     \       \ ')
        print('              \         /          \      /  \       /       \      /          \         /    \    /       \        /       \       |')
        print('               ---------            ------    -------         ------            ---------      ----         --------         -------|')
        print('score: ', score)
        print(spaces)
        time1 += 1
        print(time1)
        time.sleep(0.05)
        if spaces == 124:
            spaces = 1
            if score <= 0:
                score = score
            else:
                score -= 0.25
        if spaces2 <= 0:
            spaces2 = 124
            if score <= 0:
                score = score
            else:
                score -= 0.25
        if spaces3 >= 124:
            spaces3 = 1
            if score <= 0:
                score = score
            else:
                score -= 0.25
        spaces += 1
        spaces2 -= 1
        spaces3 += 2
        if time1 >= 1000:
            print('Game over!')
            print('you scored ' , score, 'points')
            break
    except (KeyboardInterrupt, SystemExit):
        if (item == 'carrot' and (spaces >= 33 and spaces <= 37)) or (item2 == 'carrot' and (spaces2 >= 33 and spaces2 <= 37)) or (item3 == 'carrot' and (spaces3 >= 33 and spaces3 <= 37)):
            print('\n'*50)
            print('                 doggy              carrot     bunny          catty              fishy         eggy          trash               \ \n\n\n') 
            print('_____________             ________                     _____          ________             __        _____            _____       \ ')
            print('             \           /        \        /\         /     \        /        \           /  \      /     \          /     \       \ ')
            print('              \         /          \carrot/  \       /       \      /          \         /    \    /       \        /       \       |')
            print('               ---------            ------    -------         ------            ---------      ----         --------         -------|')
            print('GOOD JOB!')
            score += 2
            print('Score: ', score)
            time.sleep(1)
            if (spaces >= 33 and spaces <= 37):
                item = return_item()
            if (spaces2 >= 33 and spaces2 <= 37):
                item2 = return_item()
            if (spaces3 >= 33 and spaces3 <= 37):
                item3 = return_item()
        elif (item == 'fishy' and (spaces >= 75 and spaces <= 83)) or (item2 == 'fishy' and (spaces2 >= 75 and spaces2 <= 83)) or (item3 == 'fishy' and (spaces3 >= 75 and spaces3 <= 83)):
            print('\n'*50)
            print('                 doggy              carrot     bunny          catty              fishy         eggy          trash               \ \n\n\n') 
            print('_____________             ________                     _____          ________             __        _____            _____       \ ')
            print('             \           /        \        /\         /     \        /        \           /  \      /     \          /     \       \ ')
            print('              \         /          \      /  \       /       \      /          \  fishy  /    \    /       \        /       \       |')
            print('               ---------            ------    -------         ------            ---------      ----         --------         -------|')
            print('GOOD JOB')
            score += 2
            print('Score: ', score)
            time.sleep(1)
            if (spaces >= 75 and spaces <= 83):
                item = return_item()
            if (spaces >= 75 and spaces <= 83):
                item2 = return_item()
            if (spaces >= 75 and spaces <= 83):
                item3 = return_item()
        elif (item == 'eggy' and (spaces >= 93 and spaces <= 96)) or (item2 == 'eggy' and (spaces2 >= 93 and spaces2 <= 96)) or (item3 == 'eggy' and (spaces3 >= 93 and spaces3 <= 96)):
            print('\n'*50)
            print('                 doggy              carrot     bunny          catty              fishy         eggy          trash               \ \n\n\n') 
            print('_____________             ________                     _____          ________             __        _____            _____       \ ')
            print('             \           /        \        /\         /     \        /        \           /  \      /     \          /     \       \ ')
            print('              \         /          \      /  \       /       \      /          \         /    \eggy/       \        /       \       |')
            print('               ---------            ------    -------         ------            ---------      ----         --------         -------|')
            print('GOOD JOB!')
            score += 2
            print('Score: ', score)
            time.sleep(1)
            if (spaces >= 93 and spaces <= 96):
                item = return_item()
            if (spaces >= 93 and spaces <= 96):
                item2 = return_item()
            if (spaces >= 93 and spaces <= 96):
                item3 = return_item()
        elif (item == 'doggy' and (spaces >= 13 and spaces <= 18)) or (item2 == 'doggy' and (spaces2 >= 13 and spaces2 <= 18)) or (item3 == 'doggy' and (spaces3 >= 13 and spaces3 <= 18)):
            print('\n'*50)
            print('                 doggy              carrot     bunny          catty              fishy         eggy          trash               \ \n\n\n') 
            print('_____________             ________                     _____          ________             __        _____            _____       \ ')
            print('             \           /        \        /\         /     \        /        \           /  \      /     \          /     \       \ ')
            print('              \  doggy  /          \      /  \       /       \      /          \         /    \    /       \        /       \       |')
            print('               ---------            ------    -------         ------            ---------      ----         --------         -------|')
            print('GOOD JOB!')
            score += 2
            print('Score: ', score)
            time.sleep(1)
            if (spaces >= 13 and spaces <= 18):
                item = return_item()
            if (spaces >= 13 and spaces <= 18):
                item2 = return_item()
            if (spaces >= 13 and spaces <= 18):
                item3 = return_item()
        elif (item == 'bunny' and (spaces >= 43 and spaces <= 39)) or (item2 == 'bunny' and (spaces2 >= 43 and spaces2 <= 49)) or (item3 == 'bunny' and (spaces3 >= 43 and spaces3 <= 49)):
            print('\n'*50)
            print('                 doggy              carrot     bunny          catty              fishy         eggy          trash               \ \n\n\n') 
            print('_____________             ________                     _____          ________             __        _____            _____       \ ')
            print('             \           /        \        /\         /     \        /        \           /  \      /     \          /     \       \ ')
            print('              \         /          \      /  \ bunny /       \      /          \         /    \    /       \        /       \       |')
            print('               ---------            ------    -------         ------            ---------      ----         --------         -------|')
            print('GOOD JOB!')
            score += 2
            print('Score: ', score)
            time.sleep(1)
            if (spaces >= 43 and spaces <= 39):
                item = return_item()
            if (spaces >= 43 and spaces <= 39):
                item2 = return_item()
            if (spaces >= 43 and spaces <= 39):
                item3 = return_item()
        elif (item == 'catty' and (spaces >= 59 and spaces <= 63)) or (item2 == 'catty' and (spaces2 >= 59 and spaces2 <= 63)) or (item3 == 'catty' and (spaces3 >= 59 and spaces3 <= 63)):
            print('\n'*50)
            print('                 doggy              carrot     bunny          catty              fishy         eggy          trash               \ \n\n\n') 
            print('_____________             ________                     _____          ________             __        _____            _____       \ ')
            print('             \           /        \        /\         /     \        /        \           /  \      /     \          /     \       \ ')
            print('              \         /          \      /  \       /       \ catty/          \         /    \    /       \        /       \       |')
            print('               ---------            ------    -------         ------            ---------      ----         --------         -------|')
            print('GOOD JOB!')
            score += 2
            print('Score: ', score)
            time.sleep(1)
            if (spaces >= 59 and spaces <= 63):
                item = return_item()
            if (spaces >= 59 and spaces <= 63):
                item2 = return_item()
            if (spaces >= 59 and spaces <= 63):
                item3 = return_item()
        elif (item == 'trash' and (spaces >= 104 and spaces <= 111)) or (item2 == 'trash' and (spaces2 >= 104 and spaces2 <= 111)) or (item3 == 'trash' and (spaces3 >= 104 and spaces3 <= 111)):
            print('\n'*50)
            print('                 doggy              carrot     bunny          catty              fishy         eggy          trash               \ \n\n\n ') 
            print('_____________             ________                     _____          ________             __        _____            _____       \ ')
            print('             \           /        \        /\         /     \        /        \           /  \      /     \          /     \       \ ')
            print('              \         /          \      /  \       /       \      /          \         /    \    /       \  trash /       \       |')
            print('               ---------            ------    -------         ------            ---------      ----         --------         -------|')
            print('GOOD JOB!')
            score += 2
            print('Score: ', score)
            time.sleep(1)
            if (spaces >= 104 and spaces <= 111):
                item = return_item()
            if (spaces >= 104 and spaces <= 111):
                item2 = return_item()
            if (spaces >= 104 and spaces <= 111):
                item3 = return_item()
        elif (item == 'bread' and (spaces >= 81 and spaces <= 84)) or (item2 == 'bread' and (spaces2 >= 81 and spaces2 <= 84)) or (item3 == 'bread' and (spaces3 >= 81 and spaces3 <= 84)):
            print('\n'*50)
            print('                 doggy              carrot     bunny          catty              fishy         eggy          trash               \ \n\n\n ') 
            print('_____________             ________                     _____          ________             __        _____            _____       \ ')
            print('             \           /        \        /\         /     \        /        \           /  \      /     \          /     \       \ ')
            print('              \         /          \      /  \       /       \      /          \         /    \    /       \        /       \ bread |')
            print('               ---------            ------    -------         ------            ---------      ----         --------         -------|')
            print('GOOD JOB!')
            score += 2
            print('Score: ', score)
            time.sleep(1)
            if (spaces >= 81 and spaces <= 84):
                item = return_item()
            if (spaces >= 81 and spaces <= 84):
                item2 = return_item()
            if (spaces >= 81 and spaces <= 84):
                item3 = return_item()
        """elif (item == 'fishy' or item == 'eggy' or item == 'bunny' or item == 'doggy' or item == 'catty' or item == 'trash' or item == 'bread') and (spaces >= 33 and spaces <= 37):
            print('the wrong item went into the wrong basket')
            print('you have lost the game')
            break
        elif (item == 'fishy' or item == 'carrot' or item == 'eggy' or item == 'bunny' or item == 'catty' or item == 'trash' or item == 'bread') and (spaces >= 13 and spaces <= 18):
            print('the wrong item went into the wrong basket')
            print('you have lost the game')
            break
        elif (item == 'fishy' or item == 'carrot' or item == 'eggy' or item == 'catty' or item == 'doggy' or item == 'trash' or item == 'bread') and (spaces >= 43 and spaces <= 49):
            print('the wrong item went into the wrong basket')
            print('you have lost the game')
            break
        elif (item == 'fishy' or item == 'carrot' or item == 'eggy' or item == 'bunny' or item == 'doggy' or item == 'trash' or item == 'bread') and (spaces >= 59 and spaces <= 63):
            print('the wrong item went into the wrong basket')
            print('you have lost the game')
            break
        elif (item == 'carrot' or item == 'eggy' or item == 'bunny' or item == 'catty' or item == 'doggy' or item == 'trash' or item == 'bread') and (spaces >= 75 and spaces <= 82):
            print('the wrong item went into the wrong basket')
            print('you have lost the game')
            break
        elif (item == 'fishy' or item == 'carrot' or item == 'bunny' or item == 'catty' or item == 'doggy' or item == 'trash' or item == 'bread') and (spaces >= 93 and spaces <= 96):
            print('the wrong item went into the wrong basket')
            print('you have lost the game')
            break
        elif (item == 'fishy' or item == 'carrot' or item == 'eggy' or item == 'bunny' or item == 'catty' or item == 'doggy' or item == 'bread') and (spaces >= 104 and spaces <= 111):
            print('the wrong item went into the trash can!!!!!!!!!!')
            print('you have lost the game')
            break
        else:
            print('There is no Basket!!!!!')"""
    except (KeyboardInterrupt, SystemExit):
        print('hello')
            
            
