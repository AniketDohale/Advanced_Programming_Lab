
def merge_Sort(arr):

    # Base Case
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr)//2
    left_Array = arr[:mid]
    right_Array = arr[mid:]

    left_Array = merge_Sort(left_Array)
    right_Array = merge_Sort(right_Array)

    return merge(left_Array, right_Array)


def merge(left, right):
    new_Array = []
    left_Index, right_Index = 0, 0

    while left_Index < len(left) and right_Index < len(right):

        if left[left_Index] < right[right_Index]:
            new_Array.append(left[left_Index])
            left_Index += 1

        else:
            new_Array.append(right[right_Index])
            right_Index += 1

    new_Array.extend(left[left_Index:])
    new_Array.extend(right[right_Index:])

    return new_Array


arr = [53, 123, 5, 2, 34, 1, 43]
print("Original Array -> ", arr)

sorted_Array = merge_Sort(arr)

print("Sorted Array -> ", sorted_Array)
