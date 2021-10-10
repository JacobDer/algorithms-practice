def max_heapify_subtree(arr, start_index):
    ''' Turn subarray of an array into a max heap.

    This is an in-place function. Assumes subtrees below the level where
    start_index is are already max heaps.

    Args:
        arr (list): List of numbers treated as a binary tree
        start_index (int): Index of element to treat as root vertex
    '''

    # Initialize top variable as start_index.
    top = start_index
    # Indices of left and right children.
    left = 2*start_index + 1
    right = 2*start_index + 2

    # Find the index of the largest of the root vertex and its two children,
    # and set top equal to that index.
    if left < len(arr) and arr[left] > arr[top]:
        top = left

    if right < len(arr) and arr[right] > arr[top]:
        top = right

    # Swap the original root vertex with its largest child, if necessary.
    if top != start_index:
        arr[start_index], arr[top] = arr[top], arr[start_index]

        max_heapify_subtree(arr=arr, start_index=top)


def max_heapify(arr):
    '''Turn array into a max heap.'''
    for index in reversed(range(0, len(test_arr))):
        max_heapify_subtree(test_arr, start_index=index)


def heapsort(arr):
    '''Perform heapsort on array.'''
    max_heapify(arr)

    sorted = []

    while len(arr) >= 1:
        sorted.append(arr.pop(0))
        if len(arr) > 1:
            max_heapify_subtree(arr, start_index=0)

    return sorted


if __name__ == '__main__':
    # Test.
    from random import randint

    test_arr = [randint(0, 100) for _ in range(0, 10)]
    print(test_arr)

    sorted = heapsort(test_arr)
    print(sorted)
