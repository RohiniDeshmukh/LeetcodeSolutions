class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
        return cleaned_str == cleaned_str[::-1]