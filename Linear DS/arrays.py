

"""
An array is a vector containing homogeneous elements i.e. belonging to the same data type. 
Elements are allocated with contiguous memory locations 
allowing easy modification, that is, addition, deletion, accessing of elements
"""
from array import array
from icecream import ic


"""
Traverse − print all the array elements one by one.

Insertion − Adds an element at the given index.

Deletion − Deletes an element at the given index.

Search − Searches an element using the given index or by the value.

Update − Updates an element at the given index.
"""


def print_array_items(array_data_items):  # Traverse the Array Elements
    ic("**************************************")
    for index, array_element in enumerate(array_data_items):
        ic(index, array_element)
    ic("**************************************")


array_data_items = array('i', [1, 2, 3, 4])
print_array_items(array_data_items)  # Print the Elements in the Array
array_data_items.insert(2, 89)  # Insert the elements in the Array
ic(array_data_items[3])  # Access the Element in Array data
array_data_items.remove(3)  # Remove the Element
print_array_items(array_data_items)  # Print the Elements
array_data_items[3] = 35  # Update the Array
print_array_items(array_data_items)  # Print the Elements
ic(array_data_items.index(1))  # Search the Element
