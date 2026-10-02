class Solution(object):
    def maxSubArray(self, nums):
        maxsum = nums[0]
        best = nums[0]
        for j in range(1,len(nums)):
            maxsum = max(nums[j],maxsum+nums[j])
            best = max(best,maxsum)
        return best