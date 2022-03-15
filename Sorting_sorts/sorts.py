from operator import index


sorts = {
    "Bubble Sort": True,
    "Selection Sort": True,
    "Insertion Sort": True,
    "Merge Sort": False,
    "Quick Sort": False,
    "Heap Sort": False,
    "Counting Sort": False,
    "Radix Sort": False,
    "Bucket Sort": False
}

testArray = [5, 8, 9, 4, 1]

def BubbleSort(array):

    for final in range(len(array),0,-1):
        exchange = False

        for i in range(0, final - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                exchange = True

        if not exchange:
            break


def SelectionSort(array):
    for i in range(len(array)):
        min_index = i

        for right_index in range(i + 1, len(array)):
            if array[right_index] < array[min_index]:
                min_index = right_index        

        array[i], array[min_index] = array[min_index], array[i]


def InsertionSort(array):
    for i in range(len(array)):
        current_element = array[i]

        while i > 0 and array[i - 1] > current_element:
            array[i] = array[i - 1]
            i -= 1

        array[i] = current_element

