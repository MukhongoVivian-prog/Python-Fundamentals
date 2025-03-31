def chop(list):
    list[:] = list[2:]
    return list


# Example usage
numbers = [1, 2, 3, 4, 5]
chop(numbers)
print(numbers)  # Output: [2, 3, 4]
