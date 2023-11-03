nums = [3,2,4]
target = 6

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_index = [x for x in range(len(nums))]
    seen={k:v for (k,v) in zip(nums,nums_index)}
    print(seen)
    
    
    for i in range(len(nums)):
        
        diff = target - nums[i]
        
        if diff in seen and seen[diff]!= i:
            return[seen[diff],i]
        
if __name__ == "__main__":        
    llamar = twoSum(nums, target)
    print(llamar)