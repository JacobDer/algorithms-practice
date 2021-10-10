def partition(arr, first_index, last_index):
    new_index = first_index  # Keep track of how far the pivot moved.
    if first_index < last_index:
        pivot = arr[first_index]  # Choose pivot as left element.
        for i in range(first_index+1, last_index+1):
            # If element is less than pivot, remove it and insert it to the
            # left of the pivot, update new position of the pivot.
            if arr[i] < pivot:
                to_insert = arr.pop(i)
                arr.insert(first_index, to_insert)
                new_index += 1

    return (arr, new_index)


def quicksort(arr, first_index, last_index):
    # If the array has at least two elements do the partition function on it,
    # followed by recursion.
    if first_index < last_index:
        arr, piv_index = partition(arr, first_index, last_index)

        # Recur quicksort on the elements to the left of the pivot, and the
        # elements to the right of the pivot.
        quicksort(arr, first_index, piv_index-1)
        quicksort(arr, piv_index+1, last_index)

    return arr


if __name__ == '__main__':
    # Test.
    from random import randint

    arr = [randint(0, 100) for _ in range(0, 10)]
    print(arr)

    sorted = quicksort(arr, 0, len(arr)-1)
    print(sorted)
