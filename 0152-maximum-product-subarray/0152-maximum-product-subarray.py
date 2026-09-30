class Solution(object):
    def maxProduct(self, nums):
        local_max = nums[0]
        local_min = nums[0]
        best = nums[0]
        for j in range(1,len(nums)):
            temp_max = local_max
            local_max = max(nums[j],local_max*nums[j],local_min*nums[j])
            local_min = min(nums[j],temp_max*nums[j],local_min*nums[j])
            best = max(best,local_min,local_max)
        return best