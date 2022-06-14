#include <stdlib.h>
#include <stdio.h>

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

int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    

    int* result;

    if (nums1Size > nums2Size){
       result = (int*) malloc(nums1Size*sizeof(int));    
    }
    else{
       result = (int*) malloc(nums2Size*sizeof(int)); 
    }


    qsort(nums1, nums1Size, sizeof(int), compare_ints);
    qsort(nums2, nums2Size, sizeof(int), compare_ints);

    int i = 0;
    int j = 0;
    int r = 0;

    while ((i < nums1Size) & (j < nums2Size)){

        if (nums1[i] == nums2[j]){
            result[r] = nums1[i];
            r++;
            i++;
            j++;
        }
        else if (nums1[i] < nums2[j]){
            i++;
        }
        else if (nums1[i] > nums2[j]){
            j++;
        }
    }

    *returnSize = r;
    return result;

    
}

int main(void){

    int nums1[] = {2, 6, 8, 1};
    int nums2[] = {1, 2};
    
    int size = 0;
    int* returnsize = &size;

    int *result;
    result = intersect(nums1, 4, nums2, 2, returnsize);
    
    for (int i = 0; i < size; i++){
        printf("%i ", result[i]);
    }
    printf("\n");
    
    free(result);
}