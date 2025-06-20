#Example 1
def hello(name):   #the variable inside the function is called Parameter
   print('Hello ' + name)
    #print('Howdy!')
    #print('Howdy!!!')
    #print('Hello there!')

hello('Queensly')   #the value passed in the fucntion call is known as Argument

#Example 2
def plusOne(number):
    return number + 1

newnumber = plusOne(5)
print(newnumber)

#Example 3
""" Write code that satisfies the following specs
def div_by (n, d}
n and d are ints > O
Returns True if d divides n evenly and False otherwise
Test your code with:
• n 1O and d = 3
• n = 195 and d = 13 """

def div_by(n,d):
   """ n and d are > 0"""
   if d%n == 0:  #you can also try n%d
      return True
   else:
      return False
print(div_by (10, 3))   
print(div_by (195, 13))