def binary_search(sorted_list, target_value):
    """Searches for the target element in a sorted list using the binary search algorithm.

    Parameters:
        sorted_list (list): The sorted list to search.
        target_value (any): The element to search for in the list.

    Returns:
        int: The index of the target element in the list. If the element is not in the list, returns -1.
    """
    left_index, right_index = sorted_list[0], len(sorted_list)-1
    while left_index <= right_index:
        middle_index = (left_index + right_index) // 2
        if target_value == sorted_list[middle_index]:
            return middle_index
        elif target_value < sorted_list[middle_index]:
            right_index = middle_index
        elif target_value > sorted_list[middle_index]:
            left_index = middle_index
    return -1


test_data = [i for i in range(1024)]
print(binary_search(test_data, 56))
