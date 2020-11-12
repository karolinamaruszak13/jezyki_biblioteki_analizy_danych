#InsertionSort jest sortowaniem stabilnym
#SelectionSort nie jest sortowaniem stabilnym

def insertion_sort(array):
    for i in range(len(array)):
        curr_element = array[i]
        prev_element = i - 1
        while prev_element >= 0 and array[prev_element] > curr_element:
            array[prev_element], array[prev_element+1] = array[prev_element+1], array[prev_element]
            prev_element -= 1



def selection_sort(array):
    for i in range(len(array)):
        min_el = i  # właściwie min_el_index
        for j in range(i + 1, len(array)):
            if array[j] < array[min_el]:
                min_el = j
        array[i], array[min_el] = array[min_el], array[i]





array1 = [6, 7, 2, 1, 4, 5]
array2 = [10, 2, 8, 100, -3, 4, 9]
insertion_sort(array1)
print(array1)
selection_sort(array2)
print(array2)
