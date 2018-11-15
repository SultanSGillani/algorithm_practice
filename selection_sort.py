# Selection Sort


def findsmallest(arr):
    """
    Find the smallest array first.
    :param arr:
    :return:
    """
    smallest = arr[0]  # Stores the smallest index
    smallest_index = 0  # Stores the index of the smallest value
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


"""
Use the above function in the selection sort algorithm
"""


def selectionSort(arr):  # Sorting the array
    newarr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)  # Finds the smallest element in the array and add it to the new array
        newarr.append(arr.pop(smallest))
    return newarr


# Now Sort the Array below using the new function
print(selectionSort([22, 34, 11, 99, 2, 12, 78, 10980, 33]))
