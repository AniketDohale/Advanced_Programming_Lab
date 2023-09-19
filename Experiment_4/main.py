import os
from mymod import test

print('--------------------------------------')
print("' Press Key ' -> Default 'sample.txt'")
choice = input(
    "'  Press Y  ' -> Add New File \n'  Press F  ' -> Show .txt Files \n")
print('--------------------------------------')


if choice.upper() == 'Y':
    file = input("Add Your File Name -> ")
    print('--------------------------------------')
    test(file)

elif choice.upper() == 'F':
    for file in os.listdir():
        if file.endswith('.txt'):
            print(file)
    print('--------------------------------------')
    file = input('Enter Filename -> ')
    print('--------------------------------------')
    test(file)

else:
    file = 'sample.txt'
    test(file)
