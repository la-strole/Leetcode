#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <limits.h>

int myAtoi(char * s){
    int positive = 1;
    int result = 0;
    unsigned char digital_expected = 0;

    if (strlen(s) == 0){
        return 0;
    }

    for (unsigned char i = 0; i < strlen(s); i++){
        printf("\nresult=%i, digital_Expected=%i, positive=%i", result, digital_expected, positive);
        if (digital_expected == 0){
            if (isdigit(s[i])){
                result += s[i] - '0';
                digital_expected = 1;
                continue;
            }
            else if (s[i] == ' '){
                continue;
            }
            else if (s[i] == '+'){
                digital_expected = 1;
                continue;
            }
            else if (s[i] == '-'){
                positive = -1;
                digital_expected = 1;
                continue;
            }
            else{
                return 0;
            }
        }
        else{
            if (!isdigit(s[i])){
                return result;
            }
            else{
                if (positive == 1){
                    if (result > INT_MAX / 10 || (result == INT_MAX / 10 && (s[i] - '0' > INT_MAX % 10))){
                        return INT_MAX;
                    }
                    else {
                        result = result * 10 + (s[i] - '0');
                    }
                }
                else{
                    if (result < INT_MIN / 10 || (result == INT_MIN / 10 && (-(s[i] - '0') < INT_MIN % 10))){
                        return INT_MIN;
                    }
                    else{
                        result = result * 10 - (s[i] - '0');
                    }
                }
            }
        }
    }
    return result;
}

int main(void){
    char* test_t = "-2147483649";
    printf("\nresult is %i", myAtoi(test_t));
   

}