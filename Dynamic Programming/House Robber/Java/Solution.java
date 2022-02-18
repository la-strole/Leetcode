import java.util.*;

class Solution {

  /* RECURSIVE SOLUTION */

  public int rob(int[] nums) {

    if (nums.length == 1) { return nums[0]; }
    if (nums.length == 2) { return Math.max(nums[0], nums[1]); }

    Map<Integer, Integer> memoDict = new HashMap<>();

    class Helper {
      static Integer helper(Integer index, Map<Integer, Integer> memoDict, int[] nums) {

        if (index > nums.length - 1) { return 0; }
        if (memoDict.containsKey(index)) { return memoDict.get(index); }

        memoDict.put(index, nums[index] + Math.max(helper(index + 2, memoDict, nums),
                helper(index + 3, memoDict, nums)));

        return memoDict.get(index);
      }
    }

    return Math.max(Helper.helper(0, memoDict, nums), Helper.helper(1, memoDict, nums));

  }

  /* Non-Recursive solution with list */

  public int rob2(int[] nums) {


    if (nums.length == 1) { return nums[0]; }
    if (nums.length == 2) { return Math.max(nums[0], nums[1]); }

    ArrayList<Integer> helper = new ArrayList<>(nums.length);
    for (int num : nums) {
      helper.add(num);
    }

    helper.set(2, nums[0] + nums[2]);

    for (int index = 3; index < nums.length; index++) {
      helper.set(index, nums[index] + Math.max(helper.get(index - 2), helper.get(index - 3)));
    }

    return Collections.max(helper);

  }



  public static void main(String[] args) {
    int[] testNums = {2,7,9,3,1};
    System.out.println("Result is " + new Solution().rob(testNums));
    System.out.println("Result is " + new Solution().rob2(testNums));
  }
}