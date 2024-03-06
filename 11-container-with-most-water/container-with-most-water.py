class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # area=0
        # for left in range(0,len(height)):
        #     for right in range(left+1, len(height)):
        #         width=right-left
        #         area=max(area,(width*min(height[left],height[right])))
        #         # area=max(area,(width*min(height[left],height[right])))
        # return area

        # maxarea = 0
        # for left in range(len(height)):
        #     for right in range(left + 1, len(height)):
        #         width = right - left
        #         maxarea = max(maxarea, min(height[left], height[right]) * width)

        # return maxarea
        maxarea=0
        left=0
        right=len(height)-1
        while right>left:
            width=right-left
            maxarea = max(maxarea, min(height[left],height[right])* width)
            if(height[left] <= height[right]): 
                left=left+1
            else:
                right=right-1
        return maxarea
        

                   




 
             



        #         if height[right]<=height[left]:
        #             q = height[right]
        #         else:
        #             q = height[left]
        #         area=width*q
        #         if area>max:
        #             max=area
        # return max
