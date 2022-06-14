#include <stdio.h>

void reverseString(char* s, int sSize){

   
    
    for (int i = 0, j = sSize - 1; i < j; i++, j--){
        char tmp = s[i];
        s[i] = s[j];
        s[j] = tmp;
    }

}

int main(void){
    char test_s[] = "hello";
    int sSize = sizeof(test_s) / sizeof(char);
    for (int i = 0; i < sSize; i++){
        printf("%c", test_s[i]);
    }
    reverseString(test_s, sSize);
    printf("\nafter reverse:\n");
    for (int i = 0; i < sSize; i++){
        printf("%c", test_s[i]);
    }
}