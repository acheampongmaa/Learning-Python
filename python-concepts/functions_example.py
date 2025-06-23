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

"""  
 Write a function that meets these specs.
def apply (criteria, n) :
• criteria is any func like is_even that takes in a number and returns a bool
• n is an int
Returns how many ints from O to n (inclusive) match
the criteria (i.e. return True when run with criteria)
"""
def is_even(x):
    return x%2 == 0
print(is_even(4))
       
def is_five(x):
    return x == 5

def apply (criteria, n):
   count = 0
   for i in range(n+1):
       if criteria(i):
           #print(i)
           count +=1
   return count

how_many = apply(is_even,5)
print(how_many)

how_many = apply(is_five,10)
print(how_many)

#Lambda functions are used once and can't be reused

#Example 1

""" Let's change the is_even fxn to a lambda fxn"""

lambda x: x%2 == 0

how_many = apply(lambda x: x%2 == 0, 6)
print(how_many)

#Example 2
def do_twice(n, fn):
     return fn(fn(n))

""" fn is a fxn. A lambda fxn will be used """
lambda x: x**2
print(do_twice(5, lambda x: x**2))