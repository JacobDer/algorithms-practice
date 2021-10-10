def find_minimum_index(arr, start_index):
    '''Find the index of the minimum element in an array, starting from a
    specific index.

    Args:
        arr (list): Any list of numbers
        start_index (int): Index from which to start. One of 0, 1,..., len(arr)
    '''

    for i in range(start_index, len(arr)):
        # Beginning at start_index, check if every exceeding element is less
        # than arr[i]. If every exceeding element is less than
        # arr[i], return index i.
        if [(arr[i] <= element) for element in arr[start_index:]] == [True]*len(range(start_index, len(arr))):
            return i


def selectionsort(arr):
    '''Perform selection sort algorithm on a list of numbers.'''

    # Check subarrays of arr, including elements from index i and onwards. Find
    # the minimum element, remove it, and replace it into arr at index i.
    for i in range(0, len(arr)):
        min_index = find_minimum_index(arr, start_index=i)
        min_value = arr.pop(min_index)
        arr.insert(i, min_value)


if __name__ == '__main__':
    # Test.
    from random import randint

    arr = [randint(0, 100) for _ in range(0, 10)]
    print(arr)

    selectionsort(arr)
    print(arr)
