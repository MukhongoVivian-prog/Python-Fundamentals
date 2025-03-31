scores = []

for i in range(1, 6):
    score = int(input(f"Enter score for subject {i}: "))
    scores.append(score)

sum= sum(scores)
average = sum / 5

print("The average is:", average)
        
if average>= 90 and average <= 100:
        print("Grade: A")
        
elif average>= 80 and average <= 89:
        print("Grade: B")

elif average>= 70 and average <= 79:
        print("Grade: C")

elif average>= 60 and average <= 69:
        print("Grade: D")

elif average< 60:
        print("Grade: F")
        
else:
        print("Invalid input. Please enter a valid score.")