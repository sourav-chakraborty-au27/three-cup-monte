lst = [1,0,2,4,32,5]
from random import shuffle
shuffle(lst)
lst

def list_shuffle(mylist):
    shuffle(mylist)
    return mylist

mylist = [' ', 'O', ' ']

list_shuffle(mylist)

# Now creating function for user guess

def user_guess():
    
    guess = ''

    while guess not in ['0','1','2']:
        guess = input('Guess a number "0", "1", "2": ')

    return int(guess)   

# Now we need to check the user guess and shuffle list if both matches

def check(mylist, guess):
    if mylist[guess] == 'O':
        print("You're right")
    else: 
        print("Wrong") 
        print(mylist)    

# Now creating  the order of logic

# Intial list
mylist = [' ', 'O', ' ']

#Shuffle list
shuffled_list = list_shuffle(mylist)

#User guess
guess = user_guess()

#Check guess
check(shuffled_list, guess)




