public class Solution {

    public void merge(int[] nums1, int m, int[] nums2, int n) {

        // Create pointers to max values of arrays
        int leftPointer = m - 1;
        int rightPointer = n - 1;
        int currentPointer = m + n - 1;

        // Iterate trough nums1 and nums2
        while (leftPointer >= 0 && rightPointer >= 0) {

            if (nums1[leftPointer] >= nums2[rightPointer]) {
                nums1[currentPointer] = nums1[leftPointer];
                leftPointer--;
            }
            else {
                nums1[currentPointer] = nums2[rightPointer];
                rightPointer--;
            }
            currentPointer--;
        }

        // Add right reminder (Left is here from the start)
        if (rightPointer >= 0) {
            if (rightPointer + 1 >= 0) System.arraycopy(nums2, 0, nums1, 0, rightPointer + 1);
        }

    }

