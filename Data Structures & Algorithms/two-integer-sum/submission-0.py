class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        found = False
        nums_end = (len(nums)-1)
        t_list = []

        for i, num in enumerate(nums):
            if found == True:
                break
            
            for j, num in enumerate(nums):
                
                if j != nums_end:
                    if (int(nums[i]) + int(nums[j]) == target) and (i != j):
                        
                        if i < j:
                            t_list.append(i)
                            t_list.append(j)
                        else:
                            t_list.append(j)
                            t_list.append(i)
                        
                        found = True
                        break
        return t_list  