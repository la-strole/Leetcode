import java.util.ArrayList;
import java.util.List;

class Solution {

  int[] originalArray;

  public Solution(int[] nums) {

    originalArray = nums.clone();

  }

  public int[] reset() {
    return originalArray;
  }

  public int[] shuffle() {

    int [] shuffledArray = new int[originalArray.length];

    ArrayList<Integer> listToShuffle = new ArrayList<>();

    for (int value : originalArray) {
      listToShuffle.add(value);
    }

    for (int i = 0; i < originalArray.length; i++) {
      shuffledArray[i] = listToShuffle.remove((int) (Math.random() * listToShuffle.size()));
    }


    return shuffledArray;
  }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */