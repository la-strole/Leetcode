#include <stdlib.h>
#include <stdio.h>
int* plusOne(int* digits, int digitsSize, int* returnSize){

    /* allocate space to len(didgits) + 1 elements */
    int* result = (int*) malloc((digitsSize + 1) * sizeof(int));
    /* copy array to result array*/
    for (int k = 0; k < digitsSize; k++){
        result[k] = digits[k];
    }

    int i = digitsSize - 1;
    int inc_flag = 0;
    int result_size = digitsSize;

    while (i >= 0){
        if (digits[i] + 1 < 10){
            /* no need extra space */
            result[i] = digits[i] + 1;
            inc_flag = 0;
            break;
        }
        else {
            result[i] = 0;
            i--;
            inc_flag = 1;
        }
    }
    /* if we need extra space */
    if ((i < 0) & (inc_flag == 1)){
        for (int j = digitsSize - 1; j >= 0; j--){
            result[j + 1] = result[j];
        }
        result[0] = 1;
        result_size++;
    }
    
    *returnSize = result_size;
    return result;
}

int main(void){
    int test_array[] = {9};
    int returnsize;
    int* res = plusOne(test_array, sizeof(test_array) / sizeof(int), &returnsize);
    for (int i = 0; i < returnsize; i++){
        printf("%i ", res[i]);
    }
    free(res);
}