#Example 1. Loop and list. 
# For loops iterate over values in a list and range function returns a list-like value. 
supplies = ['pens', 'staplers', 'flame-throwers', 'binder']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is : ' + supplies[i])


#Example 2. Multiple assignment
cat = ['fat', 'grey', 'loud']
size, color, disposition = cat
print(size)
print(color)
print(disposition)
   
#Example 3. Swapping variables
Firstname = 'Kyei' 
Lastname = 'Rapheal'
Firstname , Lastname = Lastname, Firstname
print(Firstname)
print(Lastname)

#Example 4. Augmented Assignment Operators
spam = 42
spam = spam + 1 

#an augmented assisgnment 
spam = 44
spam += 1
print(spam)