class Solution(object):
    def isPalindrome(self, s):
        if s == " ":
            return True
        if len(s)==1:
            return True
        s=s.lower()
        s=s.strip(" ")
        s = "".join(s)
        l = []
        for si in s:
            if si.isalnum():
                l.append(si)
        if l == l[::-1]:
            return True 
        return False