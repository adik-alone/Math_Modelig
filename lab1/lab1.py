from data_file import data, count_set

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.graphics.tsaplots import plot_acf

def dov_int(data, alpha, mean, std_dev):
    n = len(data)
    z_value = stats.norm.ppf(1 - alpha / 2)  # критическое значение

    # Доверительный интервал
    margin_of_error = z_value * (std_dev / np.sqrt(n))
    ci_lower = round(mean - margin_of_error, 4)
    ci_upper = round(mean + margin_of_error, 4)
    print(f" {1-alpha}% доверительный интервал: ({ci_lower}, {ci_upper})")

def task1(data, count):
    data = data[:count]
    # 1. Математическое ожидание
    mean = round(np.mean(data), 4)
    print(f"Математическое ожидание: {mean}")

    # 2. Дисперсия
    variance = round(np.var(data, ddof=0), 4) # Используем ddof=0 для выборочной дисперсии
    print(f"Дисперсия: {variance}")

    # 3. Среднеквадратическое отклонение
    std_dev = round(np.std(data, ddof=0), 4)
    print(f"Среднеквадратическое отклонение: {std_dev}")

    # 4. Коэффициент вариации
    cv = round((std_dev / mean) * 100, 4)
    print(f"Коэффициент вариации: {cv}%")

    # 5. Доверительные интервалы для математического ожидания
    dov_int(data, alpha=0.10, mean=mean, std_dev=std_dev)
    dov_int(data, alpha=0.05, mean=mean, std_dev=std_dev)
    dov_int(data, alpha=0.01, mean=mean, std_dev=std_dev)

    # 6. Относительные отклонения
    true_value = 206.4258 # Замените на истинное значение, если оно известно
    relative_deviation = (abs(mean - true_value) / true_value) * 100
    print(f"Относительное отклонение: {relative_deviation}%")

def task2(data):
    # Создание графика
    # data.sort()
    plt.plot(data, marker='o')  # 'marker' добавляет маркеры на график

    # Настройка графика
    plt.title("График значений последовательности data")
    plt.xlabel("Индекс")
    plt.ylabel("Значение")
    # plt.xlim(-100, 400)
    # plt.ylim(0, 700)
    plt.grid(True)

    # plt.savefig("func_seq.pdf")
    plt.show()


def task3(data):
    # Визуализация временного ряда
    plt.figure(figsize=(10, 4))
    plt.plot(data)
    plt.title('Случайный временной ряд')
    plt.xlabel('Время')
    plt.ylabel('Значение')
    plt.grid()
    plt.show()

    # Автокорреляционный анализ
    plt.figure(figsize=(10, 4))
    plot_acf(data, lags=300)
    plt.title('Автокорреляционная функция')
    plt.xlabel('Задержка')
    plt.ylabel('Автокорреляция')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    for i in count_set:
        print(f"Значения для выборки размером {i} значений")
        task1(data, i)
        print()

    task2(data)
    task3(data)