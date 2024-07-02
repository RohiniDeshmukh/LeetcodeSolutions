class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int i=0;
        int numZeroes=0;
        int result=0;

        for (int j=0;j<nums.length;j++){
           if (nums[j]==0){
            numZeroes++;
           }
           while(numZeroes>1){
            if( nums[i]==0) {
                numZeroes--;
            }
            i++;
            }
            

        result=Math.max(result,j-i+1);
        }
    return result;   
    }
}