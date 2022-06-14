public class Solution {
  public int climbStairs(int n) {

    if (n <= 3) {
      return n;
    }
    int n1 = 1;
    int n2 = 2;
    int temp;

    for (int i = 3; i < n + 1; i++){
      temp = n1;
      n1 = n2;
      n2 = n1 + temp;
    }
    return n2;
  }
}
