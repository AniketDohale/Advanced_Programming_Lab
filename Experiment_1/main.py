def get_Inputs(values):
    print("---------------------------------------")
    num = no_of_values
    i = 1
    while num>0:
        value = float(input(f"Enter {i} Value -> "))
        num = num - 1
        values.append(value)
        i = i + 1
    print("---------------------------------------")


def addition(values):
    sum = 0
    for value in values:
        sum = sum + value
    return sum


def ascending_Order(values):
    # Selection Sort
    for i in range(0, len(values)-1):
        for j in range(i+1, len(values)):
            if values[i]>values[j]:
                temp = values[i]
                values[i] = values[j]
                values[j] = temp


def frequent_Value(values):
    frequent_Dict = dict()
    for value in values:
        if not value in frequent_Dict:
            frequent_Dict[value] = 1
        else:
            frequent_Dict[value] += 1
    high_Frequency = max(frequent_Dict.values())
    high_Frequency_List =[]
    for number, freq in frequent_Dict.items():
        if freq == high_Frequency:
            high_Frequency_List.append(number)
    return high_Frequency_List

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

    values = []
    
    # For Addition
    if choice == '1' or choice == 'Addition':
        no_of_values = int(input("Number of Values -> "))
        get_Inputs(values)
        value = addition(values)
        print("Addition ->",value)
    
    # For Average
    elif choice == '2' or choice == 'Average':
        no_of_values = int(input("Number of Values -> "))
        get_Inputs(values)
        value = addition(values)
        avg = round(value/no_of_values, 2)
        print("Average ->",avg)

    # For Mean
    elif choice == '3' or choice == 'Mean':
        no_of_values = int(input("Number of Values -> "))
        get_Inputs(values)
        value = addition(values)
        mean = round(value/no_of_values, 2)
        print("Mean ->",mean)

    # For Median
    elif choice == '4' or choice == 'Median':
        no_of_values = int(input("Number of Values -> "))
        get_Inputs(values)
        ascending_Order(values)
        if no_of_values%2 != 0:
            # print("Odd")
            median = no_of_values//2
            print("Median ->",int(values[median]))
        else:
            # print("Even")
            num_1 = (no_of_values//2)
            num_2 = int(((no_of_values)/2) + 1)
            median = (values[num_1 - 1] + values[num_2 - 1])/2
            print("Median ->",int(median))

    # For Mode
    elif choice == '5' or choice == 'Mode':
        no_of_values = int(input("Number of Values -> "))
        get_Inputs(values)
        print("Mode ->",frequent_Value(values))

    # For Break
    elif choice =='X' or choice == 'Quit':
        print("Quitting..")
        break

    # For Invalid Input
    else:
        print("---------------------------------------")
        print("----- Invalid Input..Try Again.. ------")