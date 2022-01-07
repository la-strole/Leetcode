#include <stdio.h>

int maxProfit(int* prices, int pricesSize){
    
    int margin = 0;
    int valley = prices[0];
    int peak;

    for (int i = 1; i < pricesSize; i++){
        if (prices[i] < valley){
            valley = prices[i];
            continue;
        }
        else {
            peak = prices[i];
            margin += peak - valley;
            valley = peak;
        }
    }
    return margin;
}

int main(void){
    int test_array[6] = {7,1,5,3,6,4};
    printf("result=%i, expected result=7\n", maxProfit(test_array, 6));
}