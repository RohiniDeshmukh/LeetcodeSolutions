class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels=set('aeiouAEIOU')
        s=list(s)
        left=0
        right=len(s)-1

        while right>left:
            if s[left] in vowels and s[right] in vowels:
                s[left],s[right]=s[right],s[left]
                left=left+1
                right=right-1
            elif s[right] in vowels:
                left=left+1
            elif s[left] in vowels:
                right=right-1
            else:
                left=left+1
                right=right-1
            
        return '' .join(s)














        # arr=list(s)
        # new_array=[]
        # n=len(arr)
        # for i in range(n):
        #   if arr[i]=="a" or arr[i]=="e" or arr[i]=="i"or arr[i]=="o" or arr[i]=="u" or arr[i]=="A" or arr[i]=="E" or arr[i]=="I"or arr[i]=="O" or arr[i]=="U":
        #         new_array.append(arr[i])

        # new_array.reverse()
        # vowel_count=0
        
        # for i in range(n):
        #     if arr[i]=="a" or arr[i]=="e" or arr[i]=="i"or arr[i]=="o" or arr[i]=="u" or arr[i]=="A" or arr[i]=="E" or arr[i]=="I"or arr[i]=="O" or arr[i]=="U":
        #         arr[i]=new_array[vowel_count % len(new_array)]
        #         vowel_count=vowel_count+1
                
        # out= ''.join(arr)
        # return out


        