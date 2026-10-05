class Solution(object):
    def subarraySum(self, nums, k):
        cursum = 0
        seen = {0:1}
        count = 0
        for num in nums:
            cursum+=num
            if cursum-k in seen:
                count+=seen[cursum-k]
            seen[cursum] = seen.get(cursum,0)+1
        return count  
        