import timeit
import threading

# For Single Thread


def single_Thread(byte, filename):
    count = 0
    file = open(filename, 'rb')
    # for line in file.readline():
    #     print(line)
    byte_To_Check = bytes([byte])
    # print(byte_To_Check)
    while True:
        byte_Read = file.read(4096)
        if not byte_Read:
            break
        count += byte_Read.count(byte_To_Check)
    return count


# For Multi Thread
def multi_Thread(byte, filename, num_threads=4):
    def count_in_thread(byte, filename, start, end, result):
        count = 0
        with open(filename, 'rb') as file:
            file.seek(start)
            chunk = file.read(end - start)
            byte_to_check = bytes([byte])
            count = chunk.count(byte_to_check)
        result.append(count)

    results = []
    with open(filename, 'rb') as file:
        file_size = file.seek(0, 2)
        chunk_size = file_size // num_threads
        threads = []

        for i in range(num_threads):
            start = i * chunk_size
            end = start + chunk_size if i < num_threads - 1 else file_size
            thread = threading.Thread(target=count_in_thread, args=(
                byte, filename, start, end, results))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    return sum(results)


if __name__ == '__main__':
    print('---------------------------------------------')
    byte = int(input("Enter Byte -> "))
    file_Name = input("Enter Filename -> ")
    print('---------------------------------------------')
    print("ASCII Character-> ", chr(byte))
    print('---------------------------------------------')

    print("Running Single Threaded Count -> ", single_Thread(byte, file_Name))

    print(timeit.timeit(lambda: single_Thread(byte, file_Name), number=1))

    print('---------------------------------------------')

    print("Running multi-threaded count -> ", multi_Thread(byte, file_Name))

    print(timeit.timeit(lambda: multi_Thread(byte, file_Name), number=1))
