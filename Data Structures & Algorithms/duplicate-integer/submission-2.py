class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        flag = False
        
        set_nums = set(nums)

        if len(nums) != len(set_nums):
            flag = True
        
        return flag
        

