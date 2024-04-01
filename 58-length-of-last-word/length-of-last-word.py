class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        n=len(s)
        words=s.split()
        last_word= words[-1]
        return len(last_word)