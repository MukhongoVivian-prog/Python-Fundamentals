""""
Inheritance in Object oriented programming language
OOP
"""
class Phone():
    width =30
    height = 50
    color = 'White'
    # def __init__(self, width, height, color):
        # self.width = width
        # self.height = height
        # self.color = color
    def printColor(self):
        print("phone color: " + self.color)
class Samsung(Phone):
    brand = 'samsung'

Phone = Samsung()
print(Phone.color)
Phone.printColor() 
           