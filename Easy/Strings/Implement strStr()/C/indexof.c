#include <stdio.h>
#include <string.h>

int strStr(char * haystack, char * needle){
    char * result =  strstr(haystack, needle);
    if (strlen(needle) == 0){
        return 0;
    }
    if (result - haystack >= 0){
        return result - haystack;
    }
    else{
        return -1;
    }

}

int main(void){
    char* test_haystack = "hello";
    char* test_needle = "";
    printf("answer is %i", strStr(test_haystack, test_needle));
}