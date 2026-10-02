class Solution(object):
    def characterReplacement(self, s, k):
        maxfreq = 0
        char_count = {}
        best = 0
        i = 0 
        for j in range(len(s)):
            char_count[s[j]]=char_count.get(s[j],0)+1
            maxfreq = max(maxfreq,char_count[s[j]])
            while (j-i+1)-maxfreq>k:
                char_count[s[i]]-=1
                i+=1
            best=max(best,j-i+1)
        return best
        