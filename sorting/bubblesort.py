def bubblesort(arr):
    '''Performs bubble sort algorithm.'''

    sorting = [False] * (len(arr)-1)
    while sorting != [True] * (len(arr)-1):
        # Pass once over all elements, swapping as necessary.
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                # Swap elements.
                left = arr.pop(i)
                right = arr.pop(i)
                arr.insert(i, right)
                arr.insert(i+1, left)

        # Check each element to see if it less than or equal to the next.
        for i in range(0, len(arr)-1):
            if arr[i] <= arr[i+1]:
                sorting[i] = True
            else:
                sorting[i] = False

    return arr


if __name__ == '__main__':
    # Test.
    from random import randint

    arr = [randint(0, 100) for _ in range(0, 10)]
    print(arr)

    sorted = bubblesort(arr)
    print(sorted)
