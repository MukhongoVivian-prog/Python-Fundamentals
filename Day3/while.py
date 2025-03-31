# reating a shopping list program where the users can add remove and view items
items =[]

while True:
    action = input("What do you want to do(add, remove, view)?\n")

    if action == "add":
        new_item = input("Enter an item to add:\n")
        items.append(new_item)

    elif action == "remove":
        item_to_remove = input("Enter an item to remove:\n")
        if item_to_remove in items:
            items.remove(item_to_remove)
    
    elif action == "view":
        print("Current items in the shopping list:\n\n")
        for item in items:
            print(item)

    else:
        break #terminate the loop       