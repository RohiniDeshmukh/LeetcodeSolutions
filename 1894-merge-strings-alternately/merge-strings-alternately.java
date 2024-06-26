class Solution {
    public String mergeAlternately(String word1, String word2) {

        //abcd pq

    //abc pqr
       
        StringBuilder result= new StringBuilder();

        int minLen=Math.min(word1.length(),word2.length());

        for (int i=0;i<minLen;i++){
            result.append(word1.charAt(i));
            result.append(word2.charAt(i));
        }

        if (word1.length()>minLen){
            result.append(word1.substring(minLen));
        }

        if (word2.length()>minLen){
            result.append(word2.substring(minLen));
        }

       

         return result.toString();
        
    }
}