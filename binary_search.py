# binary search to guess a number
def binary_search(linked_list, item):
    """
    Low and High keeps Track of which part of the list
    That is tracked.
    :param linked_list:
    :param item:
    :return:
    """
    low = 0  #
    high = len(linked_list) - 1

    while low <= high:  # While you haven't narrowed it down to one element, check the middle.
        mid = (low + high)
        guess = linked_list[mid]
        if guess == item:  # Found the Item
            return mid
        if guess > item:  # Guess too High
            high = mid - 1
        else:
            low = mid + 1  # Guess too low
    return None  # The item is not there


result = [1, 2, 3, 4, 5, 8, 9, 18, 32, 50]
"""

Test Out the Function

"""
print("Element is present at index", binary_search(result, 50))  # => 9

print("Element is", binary_search(result, -1))  # => Doesn't exist
