class Solution {
    public int majorityElement(int[] nums) {
        int ans=nums[0];
        int vote=1;
        for(int n:nums)
        {
            if(n!=ans)
            {
                vote--;
                if(vote==0)
                {
                    ans=n;
                    vote=1;
                }
            }
            else
            {
                vote++;
            }
        }
        return ans;
    }
}