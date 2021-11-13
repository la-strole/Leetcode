#include <stdio.h>

void moveZeroes(int* nums, int numsSize){

    int non_zer_position = 0;

    for (int i = 0; i < numsSize; i++){
        if (nums[i] != 0){
        nums[non_zer_position] = nums[i];
        non_zer_position++;
        }
    }
    while (non_zer_position < numsSize){
        nums[non_zer_position] = 0;
        non_zer_position++;
    }
}

int main(void){
    
    int test_array[] = {1, 0, 2, 0, 0, 3, 4, 0, 5, 6, 0};
    int array_length = sizeof(test_array) / sizeof(int);
    moveZeroes(test_array, array_length);

    for (int i = 0; i < array_length; i++){
        printf("%i ", test_array[i]);
    }
}