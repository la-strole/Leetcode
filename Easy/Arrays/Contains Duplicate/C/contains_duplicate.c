#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

bool containsDuplicate(int* nums, int numsSize){

    int *seen = (int*)malloc(sizeof(int) * numsSize);
    int seen_index = 0;
    for (int i = 0; i < numsSize; i++){
        for(int j = 0; j < seen_index; j++){
            if (nums[i] == seen[j]) return true;
        }
        seen[seen_index] = nums[i];
        seen_index++;
    }
    free(seen);
    return false;
}

/* function for qsort */
int compare(const void *arg1, const void *arg2){
    return *(int*)arg1 > *(int*)arg2;
}
bool containsDuplicate_v2(int* nums, int numSize){
    /* sort array */
    qsort(nums, numSize, sizeof(int), compare);

    for (int i=0; i < numSize - 1; i++){
        if (nums[i] == nums[i+1]) return true;
    }
    return false;
}


int main(void){
    int test_array[10] = {1, 2, 3, 4, 5, 2, 7, 8, 9, 0};
    printf("Array contains duplicates: %s\n", containsDuplicate(test_array, 10) ? "True" : "False");
    printf("Array contains duplicates v 2: %s\n", containsDuplicate_v2(test_array, 10) ? "True" : "False");
}