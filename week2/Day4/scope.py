"""
SCOPE
# what is scope?
this is the extend of the are or subject that something deals with or which it is relevant to
the region in which somethig is relevant
1. Local scope
2. Global scope

"""
# 
name = "Emmanuel"

def printWelcomeMessage():
    name = "James" # private varialbe name
    print("Welcome, " + name)


printWelcomeMessage()
print(name) # Emmanuel

print("My new name is " + name)
