class Solution(object):
    def maxArea(self, height):
        ma = float('-inf')
        i,j=0,len(height)-1
        while i<j:
            a = (j-i)*min(height[i],height[j])
            ma = max(ma,a)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return ma
        