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






