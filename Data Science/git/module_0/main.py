import numpy as np


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count) # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    # random_array = np.random.randint(1,101, size=(1000))
    random_array = np.random.randint(1,101, size=(1))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    p2 = None
    while number != predict:
        count+=1
        if number > predict:
            if p2 is None:
                p2 = 100
            # predict += 1
        elif number < predict:
            if p2 is None:
                p2 = 1
            # predict -= 1
        ptemp = predict
        print(f'number={number}, predict={predict}, p2={p2}')
        predict = round((predict + p2) / 2)
        p2 = ptemp
        print(f'number={number}, predict={predict}, p2={p2}')
        if count > 100:
            exit(1)
    return(count) # выход из цикла, если угадали

score_game(game_core_v1)
score_game(game_core_v2)
# score_game(game_core_v3)

def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val<lys[mid]:
                last = mid -1
            else:
                first = mid +1
    return index

print(BinarySearch([10,20,30,40,50], 20))