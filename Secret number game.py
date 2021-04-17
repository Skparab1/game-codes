from random import randint
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

  

