#List

# Example
spam= [['cat', 'dog', 'bat'],['Yaw', 'Ama', 'Kobby']]
print(spam)
print(spam[0][1])
print(spam[1][2])
print(spam[0][-1])

# Example 2
spam= ['cat', 'dog', 'bat', 'elephant']
# print(spam[0])

# Slices
print(spam[1:3])
print(spam[:3])

# Updating a list
# Example 1
spam[0]= 'lion'
print(spam)

# Example 2
spam[1:3]= ['mouse', 'rat', 'rabbit']
print(spam)

# Deleting a value from a list
del spam[1]
print(spam)

# string and list similarities

# Example 1
greet= 'Hello'
print(len(greet))

# Example 2
greet = 'Hello ' + 'World'
print(greet)

# Example 3
num = [1, 2, 4] + [5,6,7]
print(num)

# Example 4
num = [1, 2, 4] * 3
print(num)
# List function
greet = 'Hello'
print(list(greet))

# using 'in' and 'not in' to find if a value is in or not in a list
# Example 1
find= 'cat' in spam
print(find)

# Example 2
find= 'cat' not  in spam
print(find)


"""Write a function that meets these specs:
def sum and_prod (L) :
 L is a list of numbers
Return a tuple where the first value is the
sum of all elements in L and the second value
is the product of all elements in L """


L= [1,2,3,4,5,6,7,8]
def sum_and_prod (L):
   
    sum = 0
    prod = 1
    for i in L:
        sum += i
        prod *=i
        # print(prod)
    return (sum, prod)

print(sum_and_prod(L))

"""• Write a function that meets these specs:
def make ordered list (n) :
n is a positive int
Returns a list containing all ints in order
from O to n (inclusive)"""

a = []
def make_ordered_list(n):
    for i in range (n+1):
        a.append(i)
    return a

print(make_ordered_list(10))


"""
• Write a function that meets the specification.
def remove_elem (L, e) :
L is a list
e is an object, that's it can be any number 
Returns a new list with elements in the same order as L,
but without any elements equal to e.
L=[1,2,2,2]
prints (remove_elem(L,2)) #prints [1]
"""

L=[1,2,2,2]
newlist=[]
def remove_elem(L,e):
    for i in L:
        if i != e:
            newlist.append(i)
    return newlist        
      

print(remove_elem(L,1))


"""   
• Write a function that meets these specs:
def count words (sen) :
sen is a string representing a sentence
Returns how many words are in s (i.e. a word is a
sequence of characters between spaces.
Take a string (sen) like "Hello it's me" and figure out:
How many space-separated groups (words) it contains.
print (count words ("Hello it's me"))
"""
def count_words(sen):
      s = len(sen.split(" "))
      return s
    # return len(s)
print (count_words ("Hello it's me"))


"""• Write a function that meets these specs:
def sort words (sen) :
sen is a string representing a sentence
Returns a list containing all the words in sen but
sorted in alphabetical order.
print (sort words ("look at this photograph") ) """

def sort_words(sen):
    #   s = list(sen)
      s = sen.split(" ")
      s.sort()
      return s
print(sort_words ("look at this photograph"))