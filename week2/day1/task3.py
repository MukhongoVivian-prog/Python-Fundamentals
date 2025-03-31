"""
Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs
$3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for
60 copies?
"""

# price of the book $24.95
# bookstores get 40% discount **(40*price_of_book)/100** -- disconunted price
# shipping cost for first book is $3
# remaining book we ship at 75 cents per book

# what is total wholesale cost for 60 books
# book 1 shipping is $3
# remaining 59 books will ship at 75 cents per book

# total wholesale cost
# 1) you need to caculate 40% book discounted price
# 2) total cost for 60 books = discounted price * 60
# 3) first book shipping cost $3 so we do total cost + $3
# 4) subsequent shipping cost 75 cents ($0.75) shipping cost = 59 * 0.75
# 5) total cost + shipping cost 
# 6) return total cost

def total_cost_for_copies(copies):
    price_of_book = 24.95
    discount = (40 * price_of_book) / 100  
    discounted_price = price_of_book - discount  
    
    total_book_cost = discounted_price * copies  
    
    first_book_shipping = 3  
    additional_books_shipping = (copies - 1) * 0.75  
    
    total_cost = total_book_cost + first_book_shipping + additional_books_shipping  
    
    return (total_cost)  


cost = total_cost_for_copies(60)
print(f"Total wholesale cost for 60 books: ${cost}")
