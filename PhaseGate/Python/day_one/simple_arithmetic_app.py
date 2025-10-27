import random

print("Welcome to Simple Arithmetic App")
score = 0


for i in range(1, 2): 
    number_one = random.randint(0, 50)
    number_two = random.randint(0, 50)
    print(f"\n{number_one} - {number_two} =")  

    
    for attempt in range(1, 4): 
        
            answer = int(input("Answer: "))
            if answer == number_one - number_two: