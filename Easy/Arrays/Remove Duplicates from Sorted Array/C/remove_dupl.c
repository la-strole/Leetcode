#include <stdlib.h>
#include <stdio.h>
int removeDuplicates(int* nums, int numsSize){
int point_1 = 1;
int point_2 = 0;
for (;point_1 < numsSize; point_1++){
    if (nums[point_1] != nums[point_1 - 1]){
        point_2++;
        nums[point_2] = nums[point_1];
    }
}
return point_2 + 1;
}

int main(void){
    
    int array_len = 20;
    int numbers[array_len];
    for (int i=0; i < array_len; i++){
        numbers[i] = 100 - (rand() % 200);
    }
    printf("array length %i", removeDuplicates(numbers, array_len));

}