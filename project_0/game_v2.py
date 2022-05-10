import numpy as np

def random_predict(number:int) -> int:
    """"""


    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)


def score_game(random_predict):
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=1000)
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Your algorithm guesses in {score} attempts on the average')
    return score


score_game(random_predict)        
