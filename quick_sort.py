
def quicksort(array):
    """
    Quick Sort
    :param array:
    :return:
    """
    if len(array) < 2:
        return array
    else:  # Base case: arrays with 0 or 1 element are already “sorted.”
        pivot = array[0]  # Recursive case.
        less = [i for i in array[1:] if i <= pivot] # Base case: arrays with 0 or 1 element are already “sorted.”
        greater = [i for i in array[1:] if i > pivot] # Sub-array of all the elements greater than the pivot

    return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3, 44, 1]))
