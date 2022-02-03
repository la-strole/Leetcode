public class Solution {
    public int firstBadVersion(int n) {
        int low = 1;
        int hi = n;

        while (low < hi) {
            int mid = low + (hi - low) / 2;
            if (isBadVersion(mid) == true) {
                hi = mid;
            }
            else {
                low = mid + 1;
            }
        }
        return low;
    }
}
