class Solution(object):
    def lengthOfLongestSubstring(self, s):
        w = set()
        best = 0
        i= 0
        for j in range(len(s)):
            while s[j] in w:
                w.remove(s[i])
                i+=1
            w.add(s[j])
            best = max(best,j-i+1)
        return best
        