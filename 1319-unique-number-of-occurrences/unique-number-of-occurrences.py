class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        mydict={}

        for num in arr:
            if num not in mydict:
                mydict[num]=1
            else:
                mydict[num]=mydict[num]+1

        unique=set(mydict.values())

        if len(mydict.values())==len(unique):
            return True 
        else:
            return False
