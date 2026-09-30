class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = nums[0]
        best = nums[0]
        for j in range(1,len(nums)):
            cur_sum = max(nums[j],cur_sum+nums[j])
            best = max(best,cur_sum)
        return best
        
        