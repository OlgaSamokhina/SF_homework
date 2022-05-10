import numpy as np
number = np.random.randint(1,101)
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100"))
    
    if predict_number > number:
        print("The number should be less")
        
    elif predict_number < number:
        print("The number should be more")
        
    else:
        print("The number is correct")
        break