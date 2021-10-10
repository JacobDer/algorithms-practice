def insertionsort(arr):
    for i in range(0, len(arr)):
        # Compare arr[i] to all arr[j] preceding it. If arr[i] < arr[j] for
        # some j, insert arr[i] into the j-th position, repeat.
        for j in range(0, i):
            if arr[i] < arr[j]:
                to_insert = arr.pop(i)
                arr.insert(j, to_insert)

                break


if __name__ == '__main__':
    # Test
    from random import randint
    arr = [randint(0, 100) for _ in range(0, 10)]
    print(arr)

    insertionsort(arr)
    print(arr)
