#This is a guess the munber game
import random
print('Hello! What is your name?')
name=input()
secretNum= random.randint (1, 20)
print('Well ' + name + ', I am thinking of a number between 1 and 20.')

#print('DEBUG: the secret number is ' + str(secretNum))

#Ask player to guess a number 6 times
for guessesTaken in range (1, 7):
    print( 'Take a guess.')
    guess=int(input())
    if guess < secretNum:
        print('Your guess is too low.')
    elif guess > secretNum:
        print('Your guess is too high.')  
    else:
        break  #this condition is the correct guess
if guess == secretNum:
    print('Good job ' +name + ' !. You guessed my number in ' + str(guessesTaken) + ' guesses' )  
else:
    print('Nope. The number I was thinking of was ' +str(secretNum))            

