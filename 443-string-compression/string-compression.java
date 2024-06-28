class Solution {
    public int compress(char[] chars) {

        if (chars== null || chars.length==0){ 
            return 0;
        }

        int i=0;
        int j=0;

        while (j< chars.length){
           char currentChar=chars[j];
           int count=0; 
            while (j<chars.length && chars[j]==currentChar){
                j++;
                count++;
            }
        
        chars[i]=currentChar;
        i++;

        if (count>1){
            for(char c: String.valueOf(count).toCharArray()){
                chars[i]=c;
                i++;
            }        
        }
   
    }
    return i;
    }
}