class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        s = []
        ans = [-1] * n
        for i in range(2 * n):              # go around twice
            idx = i % n                        # wrap index back into range
            while s and nums[idx] > nums[s[-1]]:
                top = s.pop()
                ans[top] = nums[idx]
            if i < n:                             # only push indices during the FIRST pass
                s.append(idx)
        return ans
            