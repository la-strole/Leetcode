public class Solution {
  public int maxSubArray(int[] nums) {

    int global_maximum = nums[0];
    int current_maximum = nums[0];

    for (int i = 1; i < nums.length; i++) {
      int num = nums[i];
      current_maximum = Math.max(current_maximum + num, num);
      global_maximum = Math.max(global_maximum, current_maximum);
    }
    return global_maximum;
  }

  public static void main(String[] args) {
    int[] testArray = {-2,1,-3,4,-1,2,1,-5,4};
    System.out.printf("Result is %d%n", new Solution().maxSubArray(testArray));
  }
}
