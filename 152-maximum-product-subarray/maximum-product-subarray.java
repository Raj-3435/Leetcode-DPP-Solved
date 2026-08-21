class Solution {
    public int maxProduct(int[] nums) {
        int maxDp[] = new int[nums.length];
        int minDp[] = new int[nums.length];

        maxDp[0] = nums[0];
        minDp[0] = nums[0];

        int ans = nums[0];
        for (int i=1;i<nums.length;i++){
            maxDp[i] = Math.max(nums[i],Math.max(nums[i]*maxDp[i-1],nums[i]*minDp[i-1])); 
            minDp[i] = Math.min(nums[i],Math.min(nums[i]*maxDp[i-1],nums[i]*minDp[i-1])); 
            ans = Math.max(ans,maxDp[i]);
        }
        return ans; 
    }
}