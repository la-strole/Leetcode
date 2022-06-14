#include <stdio.h>

int removeElement(int* nums, int numsSize, int val){
    int point_1 = 0;
    int point_2 = 0;
    while (point_2 < numsSize){
        if (nums[point_2] != val){
            nums[point_1] = nums[point_2];
            point_2++;
            point_1++;
            
            continue;
        }
        else {
            point_2++;
            if (point_2 == numsSize){
                return point_1;
            }
            while (nums[point_2] == val){
                point_2++;
                if (point_2 == numsSize){
                    return point_1;
                }
            }
            nums[point_1] = nums[point_2];
            point_1++;
            point_2++;
        }
    }
    return point_1;
}

int main(void){
    int array[4]={2,3,2,3};
    int value = 3;
    printf("\n");
    printf("\nlen of array = %i\n", removeElement(array, 4, value));
    for (int i = 0; i < 4; i++){
        printf("%i ",array[i]);
    }
}