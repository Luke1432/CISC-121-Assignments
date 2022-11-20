
"""
-------------------------------------------------------
This function sorts the numbers in a list entered as argument

-------------------------------------------------------
Parameters:
list_to_sort #list of elements to sort
Returns:
list_to_sort #same list, but sorted
-------------------------------------------------------
"""
def selection_sort(list_to_sort):
    n = len(list_to_sort) #number of elements in list_to_sort

    for m in range(n - 1): #for every element in the list
        current_min = m #set the minimum to the current value
        for i in range(m + 1, n): #for every element after the current minimum
            if list_to_sort[i] < list_to_sort[current_min]: #if the element is smaller than the current_min
                current_min = i #set that value to be the new current minimum
        if current_min != m: #if the current minimum is not m
            list_to_sort.insert(m, list_to_sort.pop(current_min))  # Line 18 (replacement) place every element in the list after the current minimum (23-25
            for k in range(m - current_min):
                list_to_sort.insert(m + 1, list_to_sort.pop(list_to_sort[k]))

    return list_to_sort #return the sorted list

#examples of lists to sort
my_list = [4, 3, 46, 7, 500, 232, 51]
my_list_2 = [7, 456, 1000, 1256, 123, 78, 1]
my_list_3 = [67 ,32, 16, 864, 34]

#sort the lists
my_list = selection_sort(my_list)
my_list_2 = selection_sort(my_list_2)
my_list_3 = selection_sort(my_list_3)


#print the sorted list
print(my_list)
print(my_list_2)
print(my_list_3)
