#Example 1
#spam = 42 #global variables are outside a function. spam here is a global variable

#def eggs():   
    #spam=42   #local scopes are inside a function.spam is a local variable
    #return spam

#results = eggs()
#print(results)

#In example 1, it's the spam in the local scope that's executed. Nothing happens to the global variable since it's referenced.

#Example 2
#spam = 42 #global variables are outside a function. spam here is a global variable

#def eggs():  
    #print('The global scope is', spam)
#eggs()    

#In example 2, the global scope is referenced in the function and it's executed.

#Example 3
spam = 42 #global variables are outside a function. spam here is a global variable

def eggs():  
    global spam 
    spam= 'Hello'  
    print(spam)
eggs()   

#In example 3, the global scope variable is modified inside the local scope and hello is printed instead of 42



