#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>

bool isPalindrome(char * s){
    
    /* format string */
    char* format_string = (char*) malloc(strlen(s) * sizeof(char));

    __int32_t j = 0;

    for (__int32_t i = 0; s[i] != '\0'; i++){
        if (isalnum(s[i])){
            format_string[j] = tolower(s[i]);
            j++;
        }
    }

    /* if it is palindrome */

    for (__int32_t i = 0; i < j / 2; i++){
        if (format_string[i] != format_string[j - 1 - i]){
            free(format_string);
            return false;
        }
    }
    free(format_string);
    return true;


    
}

int main(void){
    char* test_s = "A man, a plan, a canal: Panama";
    printf("string is palindrome? - %i", isPalindrome(test_s));
}