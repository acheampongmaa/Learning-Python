#List has different methods
# 1. index method. It shows the index of a value in a list
#Example 
spam=['hello', 'how', 'are', 'you', 'doing']
output=spam.index('hello')
print(output)


# 2. append method. It adds another value to the list
#Example 
pets = ['cat', 'dog', 'parrot']
pets.append('hamster')
print(pets)

#3. insert method. It adds another value at a specific index
#Example 
pets = ['cat', 'dog', 'parrot']
pets.insert( 2, 'hamster')
print(pets)

#4. remove method. It helps you specify a value you want to remove unlike the delete(del)
# in case there are duplicates of a value, it only removes the first instance
#Example 
pets = ['cat', 'dog', 'parrot']
pets.remove('dog')
print(pets)

#5. sort method 
#Example 1
spam = [2, 4, 3.24, -7, 9]
spam.sort ()
print (spam)

#Example 2
animals= ['cat', 'bat', 'rat', 'ant', 'cocroach']
animals.sort()
print(animals)

#Example 3. When one has a list having both capital and lower case, 
# the sort methods gives preference to the capital letters
animals= ['Cat', 'bat', 'rat', 'ant', 'cocroach', 'Sheep', 'cat']
animals.sort()
print(animals)

#to ensure it's sorted in true alphabetical order the 'key' argument is passsed
animals= ['Cat', 'bat', 'rat', 'ant', 'cocroach', 'Sheep', 'cat']
animals.sort(key=str.lower)
print(animals)