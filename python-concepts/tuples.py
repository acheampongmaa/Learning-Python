"""  
• Write a function that meets these specs:
• Hint: remember how to check if a character is in a string?
def char counts (s) :
s is a string of lowercase chars
Return a tuple where the first element is the
number of vowels in s and the second element
is the number of consonants in s
"""

# Method 1
def char_counts(s):   
      v_count=0
      c_count=0
      vowels = "aeiou"
      consonants = "bcdfghjklmnpqrstvwxyz"
      for char in s:
            if char in  vowels:
                  v_count += 1
            elif char in consonants:
                  c_count += 1 
      return ( v_count,c_count)


# print(char_counts('emmanuel'))

#  Method 2
def char_counts(s):
        vowels = "aeiou"
        (v_count, c_count)= (0,0)
        for char in s:
            if char in vowels:
                  v_count += 1
            else:
                  c_count += 1 
        return ( v_count,c_count)


print(char_counts('emmanuel'))


# """ Taking multiple arguments """
# #Method 1 tuple is used behind the scenes when * is used 
def mean (*arg):
      total=0
      for a in arg:
            total += a
      return total/len(arg)

print(mean(2,4,6))

#Method 2 assuming arg is a tuple itself
def mean (arg):
      total=0
      for a in arg:
            total += a
      return total/len(arg)

print(mean((1,2,2,4,6,7)))


# Example 3
"""
• Write a function that meets these specs:
• Use a loop and string methods to solve it.
def count_digits_and_letters(s):
    s is a string of any characters (letters, numbers, symbols)
    Return a tuple where the first element is the
    number of letters in s, and the second element
    is the number of digits in s
"""
def count_digits_and_letters(s):
      (d_count, l_count) = (0,0)
      for elements in s:
            if elements.isalpha():
                  l_count += 1
            elif elements.isdigit():
                  d_count +=1
      return   (d_count, l_count)   

print(count_digits_and_letters("you890aregoing 456799jakals!~"))