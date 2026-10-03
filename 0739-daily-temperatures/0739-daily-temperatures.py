class Solution(object):
    def dailyTemperatures(self, temperatures):
        t = temperatures
        n = len(t)
        ans = [0]*n
        s = []
        for i in range(n):
            while s and t[i]>t[s[-1]]:
                idx = s.pop()
                ans[idx] = i-idx
            s.append(i)
        return ans        