import numpy as np


def task_1():
    print("1: Одномерные массивы. Кортеж")
    r_tuple = (12.5, 4.0, 15.2, 8.8, 20.0, 6.5, 12.0, 25.0)


    r_total_classic = sum(r_tuple)



    print(f"Сопротивления элементов цепи: {r_tuple}")
    print(f"Общее сопротивление (sum): {r_total_classic:.2f} Ом")

def task_2():
    print("2: Двумерные массивы")
    matrix = np.array([
        [5,  8, 12],
        [3,  7,  8],
        [14, 2,  9]
    ])
    print("Исходная матрица:")
    print(matrix)
    values, counts = np.unique(matrix, return_counts=True)
    has_one_pair = np.sum(counts == 2) == 1
    no_higher_repeats = np.all(counts <= 2)
    has_only_two = bool(has_one_pair and no_higher_repeats)

    if has_only_two:
        dup_val = values[counts == 2][0]
        print(f"Результат: Да. В массиве ровно два одинаковых элемента (число {dup_val} встречается 2 раза).")
    else:
        print("Результат: Нет. Условие не выполнено.")
    print(f"Ответ: {has_only_two}\n")

def task_3():
    print("3: Списки")
    a_list = [10, 25, 42, 7, 88, 19, 56, 33, 90]
    print(f"Исходный список: {a_list}")

    even_slice = a_list[::2]
    print(f"Элементы с четными индексами [::2]: {even_slice}")

    print("Вывод через пробел:", *even_slice, "\n")

def task_4():
    print("4: Множества")
    numbers = [1, 2, 3, 2, 1, 4, 5, 3, 7]
    print(f"Список чисел: {numbers}")

    distinct_set = set(numbers)
    count_distinct_set = len(distinct_set)


    print(f"Множество уникальных чисел (set): {distinct_set}")
    print(f"Количество различных чисел (len(set)): {count_distinct_set}")


def task_5():
    print("5: Словари")
    text = "one two one thr two"
    print(f"Исходная строка текста: '{text}'")

    words = text.split()
    counts = {}
    result = []

    for word in words:
        prev_count = counts.get(word, 0)
        result.append(prev_count)
        counts[word] = prev_count + 1

    print("Результат подсчета предшествующих вхождений:")
    print(" ".join(map(str, result)))
    print(f"Итоговый словарь частот: {counts}\n")


if __name__ == "__main__":

    print("Вариант 1")


    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
