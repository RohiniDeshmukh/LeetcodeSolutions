class Solution {
    public String reverseVowels(String s) {

        char [] charArray=s.toCharArray();

      


        String vowels="aeiouAEIOU";

        int start=0;
        int end=s.length()-1;

        
        while (start<end){
            while(start<end && vowels.indexOf(charArray[start])==-1){
                start++;
            }
            while (start<end && vowels.indexOf(charArray[end])==-1){
                end--;
            }

            char temp=charArray[start];
            charArray[start]=charArray[end];
            charArray[end]=temp;

            start++;
            end--;
         
        }
        return new String(charArray);




        
    }
}