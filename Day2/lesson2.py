"""""
Ask the user for three inputs
first ask the user to enter a umber and store the number i a number variable
second input should ask the user to enter a number and store it in a variable called number2
third input should ask the user what operation to perform [+,-,/,*] and store it in a variable called action
if action is "+", then print the sum of the numbers
if action is "-", then print the difference of the numbers
if action is "*", then print the product of the numbers
if action is "/", then print the division of the numbers
if the action is not one of the above, print "Invalid action"

use if, elif, else to solve the problem
"""
number = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))
action = input("What action do you want to perform(+,-,*,/): ")

if action == "+":
    sum=int(number) + int(number2)
    print("The sum of the two numbers is " + str(sum))


elif action == "-":
    difference = int(number) - int(number2)
    print("The difference of the two numbers is " + str(difference))

elif action == "*":
    product = int(number) * int(number2)
    print("The product of the two numbers is " + str(product))


elif action == "/":
    quotient = int(number) / int(number2)
    print("The quotient of the two numbers is " + str(quotient))

else:
    print("Invalid action")
