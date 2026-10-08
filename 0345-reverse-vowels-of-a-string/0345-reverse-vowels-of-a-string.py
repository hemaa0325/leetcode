class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i = 0
        j = len(s)-1
        while i<j:
            if s[i].lower() not in "aeiou":
                i+=1
                continue
            if s[j].lower() not in "aeiou":
                j-=1
                continue

            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
            
        return "".join(s)
        