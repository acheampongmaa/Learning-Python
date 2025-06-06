'''  Create a contact book that stores names and phone number and allows search'''

#Creating the contact book
contact_book= {}

while True:
    print("\nAdd a new contact:")
    userFN = str(input ("Enter your firstname: ").capitalize())
    userLN = str(input("Enter your lastname: ").capitalize())
    userNum= int(input("Enter your phone number: "))
    user_fullName = userFN + " " + userLN 
    contact_book[user_fullName] = userNum
    
    ask_more = input("Do you want to add another contact? (y/n): ")
    if ask_more.lower() != "y":
        break

print("\nContact_book")
for name, number in contact_book.items():
    print(f"{name}: {number}")

#make a search in the contact book
search_name = str(input("\n Search for contact name with full name: ").title())
if search_name in contact_book:
    print(f"{search_name} is in contact book with number: {contact_book[search_name]}") 
else:
    print (f"{search_name} not found. Try again!")    