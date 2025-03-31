"""
A function to reverse a string name "Dabel"
Recursion is when a function calls itself

"""

def reverseString(name):
    if len(name) == 1:
        return name
    else:
        return reverseString(name[-1]) + reverseString(name[:-1])
    

    """
    code explnation of the above function
    - if the length of the string is 1, it means we've reached the end of the string and it's already in reverse order. So we return the string itself.
    - else, we take the last character of the string, append it to the reverse of the rest of the string (which is the result of calling reverseString with the string without the last character).
    return "Dabel" == reverseString("Dabel")  # This will return True

    name = Dabel
    reversestring(Dabel)

    l + reversestring(Dabe)
    
    """