#Example 1
#def div42by(divideBy):
    #try:
        #return 42/divideBy
    #except ZeroDivisionError:
        #print('Error: You tried to divide by zero.')

#print(div42by(21))
#print(div42by(12))
#print(div42by(0))
#print(div42by(1))


#Example 2
print('How many cats do you have?')
numCat= input()
try:
    if int(numCat) < 0:
        print('That is a negative number. Try again.')
    elif int(numCat) >=4:
        print('That is a lot of cats.')
    else:
        print('That is not many cats.')    
except ValueError:
   print('You did not enter a number.')






