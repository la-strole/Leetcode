#include <stdio.h>
#include <stdlib.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int bisection_search(int * sorted_array, int array_size, int search_target){
   
    printf("\nbisection search for %i", search_target);
    /* base cases */
    if (array_size == 1){
        if (sorted_array[0] == search_target){
            return 1;
        } 
        else{
            return 0;
        }
    }
    int middle_index = array_size / 2;
    if (sorted_array[middle_index] == search_target){
        return 1;
    }
    else if (sorted_array[middle_index] < search_target){
        return bisection_search(&sorted_array[middle_index], array_size - middle_index, search_target);
    }
    else if (sorted_array[middle_index] > search_target){
        return bisection_search(sorted_array, array_size - middle_index, search_target);
    }
    return -1;
}
int compare_ints(const void* a, const void* b)
{
    
    int arg1 = *(const int*)a;
    int arg2 = *(const int*)b;
 
    if (arg1 < arg2) return -1;
    if (arg1 > arg2) return 1;
    return 0;
 
    // return (arg1 > arg2) - (arg1 < arg2); // possible shortcut
    // return arg1 - arg2; // erroneous shortcut (fails if INT_MIN is present)
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    
    int* result_array = (int*) malloc(2 * sizeof(int)); 
    int result_size = 2;
    *returnSize = result_size;
    /*copy array */
    int* nums_copy = (int*) malloc(sizeof(nums));
    for (int i = 0; i < numsSize; i++){
        nums_copy[i] = nums[i];
    }
    /* sort array */
    qsort(nums_copy, numsSize, sizeof(int), compare_ints);

    int differ = -1;


    for (int i = 0; i < numsSize - 1; i++){
        differ = target - nums[i];
        
        if (bisection_search(nums_copy, numsSize, differ) == 1){
            
            for (int j = i + 1; j < numsSize; j++){
                if (differ == nums[j]){
                    result_array[0] = i;
                    result_array[1] = j;
                    free(nums_copy);
                    return result_array;
                }
            }
        }
        
    }
    
    result_array[0] = 0;
    result_array[1] = 0;
    free(nums_copy);
    return result_array;

}


int main(void){
    
    /* bisrction search test 
    int test_array[] = {1, 3, 5, 7, 8, 9, 10};
    int array_size = sizeof(test_array) / sizeof(int);
    int target = 10;
    printf("\nresult is %i", bisection_search(test_array, array_size, target));
    */
    int test_array[] = {3, 2, 4}; 
    int sum_of_two = 6; /* expected answer is 0, 1 */
    int return_size;
    int * result = twoSum(test_array, sizeof(test_array) / sizeof(int), sum_of_two, &return_size);
    printf("\nreturn size = %i\n", return_size);
    printf("result is [%i, %i]", result[0], result[1]);
    return 1;
}