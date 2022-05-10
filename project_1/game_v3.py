"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
Алгоритм учитывает информацию о том, больше или меньше предполагаемое (случайное) число нужного нам числа
Функция справляется с угадыванием меньше чем за 20 попыток

"""

import numpy as np


def random_predict(number: int) -> int:
    """
    Рандомно угадываем число от 1 до 100,
    учитываем больше или меньше предполагаемое число загаданного,
    минимизируем количество попыток.
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_number = 1
    max_number = 100
    predict_number = round((min_number+max_number) / 2)
    
    while True:
        count += 1
        if predict_number != number:
            if predict_number > number:
                max_number = predict_number - 1
                predict_number = round((min_number+max_number) / 2)
            elif predict_number < number:
                min_number = predict_number + 1
                predict_number = round((min_number+max_number) / 2)
        else:
            break  # выход из цикла если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


score_game(random_predict)