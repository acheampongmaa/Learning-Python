# Example 1 
name = 'Olive'
yourname = input('Please type your name:')
while name != yourname:
    print(f"It's not your name. Try again!")
    break
else: 
    print(f"It's your name!")

#Example 2
name = 'Queensly'
while True:
    yourname = input('Please type your name:')
    if name == yourname:
        break
print('Thank you!')    


# Example 3
spam = 0
while spam < 5:
    spam += 1
    if spam == 3:
     continue 
    print ('spam is ' + str(spam))