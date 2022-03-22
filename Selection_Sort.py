# From Elements find max/min element at every pass
# Place it to proper position

Number_List = [3, 50, 2, 0, 35, 11, 1, 100]

def selection_sort():
    global Number_List

    Number_List_length = len(Number_List)

    # Start from First position Onwards
    for index_pos_outer in range(Number_List_length):
        # For each pass set a Minimum element
        min_element = Number_List[index_pos_outer]

        # Start from Next position Onwards
        for index_pos_inner in range(index_pos_outer+1, Number_List_length):
            # If that element is minimum than pre-set minimum element
            # Set current minimum
            # Exchange Value
            if Number_List[index_pos_inner] < min_element:
                min_element = Number_List[index_pos_inner]
                Number_List[index_pos_outer], Number_List[index_pos_inner] = Number_List[index_pos_inner], Number_List[index_pos_outer]

selection_sort()
print(Number_List)