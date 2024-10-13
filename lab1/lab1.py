from data_file import data, count_set

import numpy as np
import scipy.stats as stats

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


if __name__ == "__main__":
    for i in count_set:
        print(f"Значения для выборки размером {i} значений")
        task1(data, i)
        print()