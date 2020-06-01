def kadane_algorith(nums):
    
    current_max = nums[0]
    global_max = nums[0]
    
    for i in range(1, len(nums)):
        
        current_max = max(nums[i], current_max+nums[i])
        
        if current_max > global_max:
            global_max = current_max
    
    return global_max

if __name__ == "__main__":
    
    nums = [1,-2,3,4,-5,8]
    print(kadane_algorith(nums))