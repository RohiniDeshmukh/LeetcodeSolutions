class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list3=nums1 +nums2
        list3.sort()
        if len(list3)%2==0:        #list is even
            part1=list3[len(list3)//2]
            part2=list3[(len(list3)//2)-1]
            part3=float(part1+part2)/2
        else:
            part3=list3[len(list3)//2] #list is odd
        return part3








        # median=list3(len[list3]/2+len[(list3/2)-1])
