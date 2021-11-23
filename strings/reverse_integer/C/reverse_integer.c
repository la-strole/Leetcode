#include <stdio.h>
#include <limits.h>

int reverse(int x){

    int answer = 0;
    
    while (x != 0){
        int last_digit = x % 10;
        if ((answer > INT_MAX / 10) || ((answer == INT_MAX / 10 && last_digit > 7)) || 
            (answer < INT_MIN / 10) || (answer == INT_MIN / 10 && last_digit < -8)){
            return 0;
        }
        answer = answer * 10 + last_digit;
        x = x / 10;
    }
    return answer;
}

int main(void){
    int test_x = 12345;
    printf("\nbefore:%i\nafter: %i", test_x, reverse(test_x));
}