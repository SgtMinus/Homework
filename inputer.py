def file_input(path):
    with open(path, 'r') as file:
        data = [float(i) for i in file.readline().split(" ")]
    return data


def console_input():
    print("Введите исходные данные")
    data = [float(i) for i in input().split(" ")]
    return data
