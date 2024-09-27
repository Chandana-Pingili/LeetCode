import java.util.Collections;
class Solution {
    public String largestNumber(int[] nums) {
        // String s=String.valueOf(nums[0]);
        // for(int i=1;i<nums.length;i++)
        // {
        //     if(((s+String.valueOf(nums[i])).compareTo(String.valueOf(nums[i])+s))>=0)
        //     {
        //         String ns=s+String.valueOf(nums[i]);
        //         s=ns;
        //     }
        //     else
        //     {
        //         String ns=String.valueOf(nums[i])+s;
        //         s=ns;
        //     }

        // }
        // return s;
        String[] array =  new String[nums.length];
        for(int i=0; i<nums.length; i++){
            array[i] = String.valueOf(nums[i]);
        }
        Arrays.sort(array,(a,b)-> (b+a).compareTo(a+b));
        if(array[0].equals("0")){
            return "0";
        }
        StringBuilder largest = new StringBuilder();
        for(int i=0; i<array.length; i++){
            largest.append(array[i]);
        }
        return largest.toString();
    }
}
