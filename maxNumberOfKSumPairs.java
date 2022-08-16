class Solution {
    public int maxOperations(int[] nums, int k) {
    int count = 0, start = 0, last = nums.length - 1;
    Arrays.sort(nums);
        while(start < last)
        {
            if(nums[start]+nums[last] == k)
            {
                start++;
                last--;
                count++;
            }
            else if(nums[start] + nums[last] < k)
                start++;
            else
                last--;
            
        }
        return count;
    }
}
