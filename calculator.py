import math
import numpy
import matplotlib.pyplot as plt


def variational(data):
    print("Вариационный ряд:")
    data.sort()
    return data


def middle_value(data):
    return sum(data) / len(data)


def standard_deviation(data):
    deviation = 0
    average_value = middle_value(data)
    for i in data:
        deviation += (average_value - i) ** 2
    deviation = math.sqrt(deviation / (len(data) - 1))
    return deviation


def empirical_distributional_function(data):
    data_without_repeats = list(set(data))
    data_without_repeats.sort()
    function = [data.count(data_without_repeats[0]) / len(data)]
    for i in range(1, len(data_without_repeats)):
        function.append(data.count(data_without_repeats[i]) / len(data) + function[i - 1])
    plt.step(data_without_repeats, function, where="post")
    plt.xlabel("x")
    plt.ylabel("F(x)")
    plt.grid(55)
    plt.show()
    return data_without_repeats, function


def get_frequencies(data):
    data_without_repeats = list(set(data))
    data_without_repeats.sort()
    amount_of_numbers = []
    frequencies = []
    for i in range(len(data_without_repeats)):
        amount_of_numbers.append(data.count(data_without_repeats[i]))
        frequencies.append(data.count(data_without_repeats[i]) / len(data))

    plt.hist(data, bins=20)
    plt.show()
    return data_without_repeats, amount_of_numbers, frequencies
