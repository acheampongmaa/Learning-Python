#This program request the user for a name and prints it backwards

#Example 1
username = input ("Enter your name: ")
reversed_name = username [::-1]
print(reversed_name)

#Example 2
username = input ("Enter your name: ")
for name in reversed(username):
    print("This is your reversed", name)

#Example 3
username = input ("Enter your name: ")
reversed_name= "".join(reversed(username))
print(reversed_name)