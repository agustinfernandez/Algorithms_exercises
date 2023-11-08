def sort_colors(nums):
    
    first_index= 0 
    second_index = len(nums) -1 
    
    i = 0

    while  i <= second_index:
       
       
       if nums[i] == 2:
           nums[second_index], nums[i] = nums[i], nums[second_index]
           second_index += -1
           
        
       elif nums[i] == 1:
           i += 1    
       
       elif nums[i] == 0 and nums[first_index] == 0:
           first_index += 1
           i += 1

       else:
           nums[i], nums[first_index] = nums[first_index], nums[i]
           first_index += 1
           

    return nums
           
           
if __name__ == "__main__":
    test = sort_colors([2,0,2,1,1,0])
    print(test)
           

           

            
           
           
           
