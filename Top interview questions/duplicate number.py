def duplicate(nums):
    
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            print("Repitition found:", abs(num))
            
if __name__ == "__main__":
    
    nums = [2,6,4,5,1,2,3]
    duplicate(nums)
