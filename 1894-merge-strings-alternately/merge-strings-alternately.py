class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n1=len(word1)
        n2=len(word2)
        merged=""

        for i in range (0,min(n1,n2)):

            merged=merged+word1[i]+word2[i]

        if n1>n2:
            merged=merged+word1[n2:]
        else:
            merged=merged+word2[n1:]

        return merged
