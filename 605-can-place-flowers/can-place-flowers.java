class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {

        
        if (flowerbed.length==1 && flowerbed[0]==0){
            return true;
        }

        int temp=0;

        for (int i=0; i<flowerbed.length; i++){
            if (flowerbed[i]==0) {
                if (i==0 && flowerbed[i+1]==0){
                    flowerbed[i]=1;
                    temp++;
                }
                if ((i>0 && i<flowerbed.length-1) && (flowerbed[i+1]==0 && flowerbed[i-1]==0)){
                    flowerbed[i]=1;
                    temp++;
                }
                if (i==flowerbed.length-1 && flowerbed[i-1]==0){
                    flowerbed[i]=1;
                    temp++;
                }


            }  

        }
                
             

        if (temp>=n){
            return true;
        }
        
        return false;    
        
    }
}
