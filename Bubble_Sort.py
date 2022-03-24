# In each pass compare adjacent elements. Push Min/Max elements to end
# Like bubble it will be pushed up

Number_List = [3, 50, 2, 0, 35, 11, 1, 100, 4, 500]

def BubbleSort():
    global Number_List

    Number_List_length = len(Number_List)

    # Start from First position Onwards
    for index_pos_outer in range(Number_List_length):
        # Start pushing the Max number towards end
        for index_pos_inner in range(0, Number_List_length-index_pos_outer-1):
            if Number_List[index_pos_inner] > Number_List[index_pos_inner+1]:
                Number_List[index_pos_inner], Number_List[index_pos_inner+1] = Number_List[index_pos_inner+1], Number_List[index_pos_inner]

BubbleSort()
print(Number_List)