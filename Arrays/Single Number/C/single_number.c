#include <stdio.h>

int singleNumber(int* nums, int numsSize){
    int sum = 0;
    for (int i = 0; i < numsSize; i++){
        sum ^= nums[i];
    }
    return sum;
}

int main(void){

    int test_array[] = {1, 1, 2, 2, 3, 4, 4};
    printf("single element is %i\n", singleNumber(test_array, 7));
}