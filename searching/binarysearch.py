def binary_search(ls, n, low_index, high_index):
    if low_index <= high_index:
        mid_index = (low_index + high_index) // 2
        element = ls[mid_index]

        # Check base case.
        if element == n:
            return mid_index
        # Recursion.
        elif element < n:
            return binary_search(ls, n, mid_index+1, high_index)
        elif element > n:
            return binary_search(ls, n, low_index, mid_index-1)
    # If not found anywhere in recursion, return -1.
    else:
        return -1


if __name__ == '__main__':
    # Test.
    ls = [0, 1, 2, 3, 5, 6, 100, 255]
    result = binary_search(ls, 100, low_index=0, high_index=len(ls))
    print(result)
