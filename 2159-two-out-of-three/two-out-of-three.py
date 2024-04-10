class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        

       # Create a set instead of a tuple
        result_set = set()
        output=[]
        # Update the set with elements from nums1, nums2, and nums3
        result_set.update(nums1)
        result_set.update(nums2)
        result_set.update(nums3)


        for num in result_set:
            if (num in nums1 and num in nums2) or (num in nums2 and num in nums3) or (num in nums1 and num in nums3):
                output.append(num)

        return output


        
        

