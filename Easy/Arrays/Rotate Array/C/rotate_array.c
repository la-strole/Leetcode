#include <stdio.h>

void rotate(int* nums, int numsSize, int k){
    if (numsSize > 0){
        int shift = k % numsSize;
        /* reverse right*/
        int tmp = 0;
        for (int i = 0; i < shift / 2; i++){
            tmp = nums[numsSize - 1 - i];
            nums[numsSize - 1 - i] = nums[numsSize - shift + i];
            nums[numsSize - shift + i] = tmp;
        }
        /* reverse left */
        tmp = 0;
        for (int i = 0; i < (numsSize - shift) / 2; i++){
            tmp = nums[numsSize - 1 - shift - i];
            nums[numsSize - 1 - shift - i] = nums[i];
            nums[i] = tmp;
        }
        /* reverse all array */
        tmp = 0;
        for (int i = 0; i < numsSize / 2; i++){
            tmp = nums[numsSize - 1 - i];
            nums[numsSize - 1 - i] = nums[i];
            nums[i] = tmp;
        }
    }
}

int main(void){

    int array[] = {1, 2, 3};
    rotate(array, 3, 1);
    for (int i = 0; i < 3; i++){
        printf("%i,",array[i]);
    }
}