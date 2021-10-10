def merge(left, right):
    merged_arr = []

    while left or right:
        # If both left and right arrays are nonempty, compare first elements,
        # and add the lesser of the two to the new array.
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                to_insert = left.pop(0)
                merged_arr.append(to_insert)
            else:
                to_insert = right.pop(0)
                merged_arr.append(to_insert)

        # If one of the arrays is empty, take advantage of the assumption that
        # the other is already sorted, and simply append the elements of the
        # nonempty array to the new array, until there are none left to append.
        elif len(left) == 0:
            while right:
                to_insert = right.pop(0)
                merged_arr.append(to_insert)

        elif len(right) == 0:
            while left:
                to_insert = left.pop(0)
                merged_arr.append(to_insert)

    return merged_arr


def mergesort(arr):
    # If arr contains 2 or more elements, split it in half, recursively split
    # the halves in half, and merge (sort) everything once the recursion ends.
    if len(arr) > 1:
        mid = round(len(arr)/2)
        left = arr[:mid]
        right = arr[mid:]

        return merge(mergesort(left), mergesort(right))

    else:
        return arr


if __name__ == '__main__':
    # Test.
    from random import randint

    arr = [randint(0, 100) for _ in range(0, 10)]
    sorted = mergesort(arr)

    print(arr, sorted, sep='\n')
