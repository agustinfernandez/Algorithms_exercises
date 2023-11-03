def merge_two_sorted_list(list_1, list_2, int_1, int_2):

    for i in range(len(list_1)-1, -1,-1):

        if int_1 == 0  or int_2 == 0:
            return list_1

        elif list_1[int_1-1] < list_2[int_2-1]:
            
            list_1[i] = list_2[int_2-1]
            int_2= int_2-1
        
        elif list_1[int_1-1] == list_2[int_2-1]:

            list_1[i] = list_2[int_2-1]
            int_2= int_2-1
        else:

            list_1[i] = list_1[int_1-1]
            int_1 = int_1-1
        
    return list_1

solution = merge_two_sorted_list([-1,2,4,0,0,0], [2,5,6], 3,3)
print(solution)






