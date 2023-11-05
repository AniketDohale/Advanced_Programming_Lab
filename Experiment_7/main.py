import re


def calculate_Expression():
    global run
    global value

    if value == 0:
        expression = input("Enter Eqation -> ")
    else:
        expression = input(str(value))

    if expression == 'X':
        value = 'Quit'
        run = False

    else:
        if expression == '':
            print(value)

        elif any(char.isdigit() for char in expression):
            expression = re.sub('[a-zA-Z,:()" "]', '', expression)

            if value == 0:
                value = eval(expression)
            else:
                value = eval(str(value)+expression)

        else:
            print("Enter Valid Numeric Input..")


print('-------------------------------')
print('X -> To Quit')
print('-------------------------------')
print('''*NOTE -> '+' -> Addition
         '-' -> Subtraction
         '*' -> Multiplication
         '/' -> Division
         '**' -> Square
         '**-1' -> Reciprocal
         '**0.5' -> Squreroot''')
print('-------------------------------')


value = 0
run = True

while run:
    calculate_Expression()
