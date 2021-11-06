"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_number = np.random.randint(1, 101)
    start = 1
    end = 100
    
# найдем загаданное число методом деления пополам
    while True:
        count += 1
        if number == predict_number:
            break
        elif predict_number < number:   # если текущее число меньше загаданного
            start = predict_number      # обрезаем начало будущих поисков и находим половину разности текущего числа и конца
            delta = int((end-predict_number)/2)
            if delta == 0:              # защита от нулевого приращения в случае деления 1 на 2 (при привидении к int будет 0)
                delta = 1
            predict_number = predict_number + delta
            continue
        elif predict_number > number:   # если текущее число больше загаданного
            end = predict_number        # обрезаем конец будущих поисков и находим половину разности текущего числа и начала
            delta = int((predict_number-start)/2)
            if delta == 0:
                delta = 1
            predict_number = predict_number - delta
            continue
        
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


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
