import java.util.ArrayList;
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {

        // candies = [2,3,5,1,3]
        ArrayList <Boolean>resultList=new ArrayList<>();

        int max=candies[0];

        for (int i=1; i<candies.length; i++){
            if (candies[i]>max){
                max=candies[i];
            }

        }

        for (int i=0; i<candies.length; i++){
            if (candies[i]+extraCandies>=max){
                resultList.add(true);
            }
            else {
                resultList.add(false);
            }

        }
        return resultList;
    }
}