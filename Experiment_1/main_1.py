from collections import Counter


def get_Inputs(num_Values):
    print("---------------------------------------")
    values = []
    for i in range(num_Values):
        value = float(input(f"Enter {i+1} Value -> "))
        values.append(value)
    print("---------------------------------------")
    return values


def addition(values):
    return sum(values)


def mean(values):
    return sum(values) / len(values)


def median(values):
    sorted_Values = sorted(values)
    length = len(sorted_Values)

    if length % 2 != 0:
        return sorted_Values[length//2]
    else:
        mid_1 = sorted_Values[length//2 - 1]
        mid_2 = sorted_Values[length//2]
        return (mid_1 + mid_2)/2


def mode(values):
    number_Counts = Counter(values)
    max_Frequency = max(number_Counts.values())
    modes = [number for number, frequency in number_Counts.items()
             if frequency == max_Frequency]

    return modes


while True:
    print("---------------------------------------")
    print("Choose Below Options :")
    print("1. Addition")
    print("2. Average")
    print("3. Mean")
    print("4. Median")
    print("5. Mode")
    print("X. Quit")
    print("---------------------------------------")

    choice = input("Choice -> ")

    if choice == 'X' or choice == 'Quit':
        print("Quitted..")
        break

    if choice == '1' or choice == 'Addition':
        num_Values = int(input("Number of Values -> "))
        values = get_Inputs(num_Values)
        result = addition(values)
        print("Addition ->", result)

    elif choice == '2' or choice == 'Average':
        num_Values = int(input("Number of Values -> "))
        values = get_Inputs(num_Values)
        result = mean(values)
        print("Average ->", result)

    elif choice == '3' or choice == 'Mean':
        num_Values = int(input("Number of Values -> "))
        values = get_Inputs(num_Values)
        result = mean(values)
        print("Mean ->", result)

    elif choice == '4' or choice == 'Median':
        num_Values = int(input("Number of Values -> "))
        values = get_Inputs(num_Values)
        result = median(values)
        print("Median ->", result)

    elif choice == '5' or choice == 'Mode':
        num_Values = int(input("Number of Values -> "))
        values = get_Inputs(num_Values)
        result = mode(values)
        print("Mode ->", result)

    else:
        print("---------------------------------------")
        print("----- Invalid Input..Try Again.. ------")
