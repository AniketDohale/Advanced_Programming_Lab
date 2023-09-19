def count_Lines(file):
    try:
        txt_File = open(file, 'r')
        lines = txt_File.readlines()
        return len(lines)
    except FileNotFoundError:
        print('--------------------------------------')
        print("File Not Found")


def count_Char(file):
    try:
        txt_File = open(file, 'r')
        chars = txt_File.read()
        return len(chars)
    except FileNotFoundError:
        print("Please Enter Valid Filename")
        print('--------------------------------------')


def test(file):
    line_Count = count_Lines(file)
    char_Count = count_Char(file)

    if line_Count != None and char_Count != None:
        print("Filename:", file)
        print(f"Lines -> '{line_Count}'")
        print(f"Characters -> '{char_Count}'")
        print('--------------------------------------')


if __name__ == '__main__':
    input_File = input("Enter Filename -> ")
    test(input_File)
