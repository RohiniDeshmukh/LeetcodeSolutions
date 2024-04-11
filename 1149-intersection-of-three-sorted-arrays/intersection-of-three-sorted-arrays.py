class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        result=[]
    
        for num in arr1:
            if num in arr2 and num in arr3:
                result.append(num)
        result.sort()
        return result
