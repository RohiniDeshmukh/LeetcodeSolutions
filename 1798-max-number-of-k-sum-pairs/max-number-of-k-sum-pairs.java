class Solution {
    public int maxOperations(int[] nums, int k) {
        

        // HashMap <Integer, Integer> map= new HashMap<>();
        // int count=0;

        // for (int i=0;i<nums.length-1;i++){
        //     map.put(nums[i],map.getOrDefault(nums[i],0)+1);
        // }

        // for (int i=0;i<nums.length-1;i++){

        //     int current=nums[i];
        //     int compliment=k-nums[i];
        //     if (map.getOrDefault(current,0)>0 && (map.getOrDefault(compliment,0)>0));{
                
        //     }

        // }


        Arrays.sort(nums);
        int count=0;
        int left= 0;
        int right=nums.length-1;

        while(right>left){
            if (nums[left]+nums[right]> k){
                right--;
            }else if (nums[left]+nums[right]<k){
                    left++;
            }else{
                left++;
                right--;
                count++;
            }
            
        }
        return count;

    }
}