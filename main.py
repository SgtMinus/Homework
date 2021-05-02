import calculator
import inputer

while True:
    input_method = int(input("Как ввести данные? Выберите номер способа\n"
                             "1. Ввод через файл\n"
                             "2. Ввод через строку\n"
                             "3. Выйти из приложения\n"))
    if input_method == 1:
        data = inputer.file_input(input("Введите путь к файлу:\n"))
    if input_method == 2:
        data = inputer.console_input()
    if input_method == 3:
        SystemExit(0)
    print("Исходные данные:")
    print(data)
    print(calculator.variational(data))
    print("Экстремальные значения вариационного ряда:")
    print(data[0], data[-1], sep="\t")
    print("Размах выборки:")
    print(data[-1] - data[0])
    print("Оценка математического ожидания:")
    print('%.4f' % calculator.middle_value(data))
    print("Среднеквадратическое отклонение:")
    print('%.4f' % calculator.standard_deviation(data))
    print("Эмпирическая функция распределения:")
    data_without_repeats, function = calculator.empirical_distributional_function(data)
    print("x", end="\t\t")
    for i in data_without_repeats:
        print(i, end="\t")
    print()
    print("F(x)", end="\t")
    for i in function:
        print('%.3f' % i, end="\t")
    print()
    print("Гистограмма и полигон частот:")
    print("x", end="\t\t")
    data_without_repeats, amount_of_numbers, frequencies = calculator.get_frequencies(data)
    for i in data_without_repeats:
        print(i, end="\t")
    print()
    print("N", end="\t\t")
    for i in amount_of_numbers:
        print('%.3f' % i, end="\t")
    print()
    print("W", end="\t\t")
    for i in frequencies:
        print('%.3f' % i, end="\t")
    print()
