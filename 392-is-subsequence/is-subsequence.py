class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        count=""
        j=0
        n=len(t)
        for i in range(0,len(s)):
            while(j<n):
                if s[i]==t[j]:
                    count=count+s[i]
                    j=j+1
                    break
                j=j+1

  
        if s==count:
            return(True)
        else:
            return(False)