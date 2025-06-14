"""   
Hardcode a number as a secret number.
Write a program that checks through all the numbers from 1 to
10 and prints the secret value if it's in that range. If it is not
found, it doesn't print anything.
How does the program look if I change the requirement to be:
If it's not found, prints that it didn't find it. """

found = False
secret_num = 7
# ask_num = int(input('Enter the secret number: '))
for num in range (1,11):
      if num == secret_num:
        #    print(f"You got the secret number right! It's {secret_num}.")
           found = True
if not found:
            print(f"Ooops!The number you entered is out of range.")
else:
        print(f"You got the secret number right! It's {secret_num}.")            
 

# guess = 7
# ask_num = int(input('Enter the secret number: ')) 
# :
# while guess == ask_num
#     print('yeah')
#     break