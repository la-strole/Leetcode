#include <stdio.h>
#include <string.h>
#include <stdbool.h>

bool isAnagram(char * s, char * t){
    
    if (strlen(s) != strlen(t)){
        return false;
    }

    /* create hash table for s */
    int hash_table[26] = {0};
    for (int i = 0; i < strlen(s); i++){
        hash_table[s[i] - 'a']++;
        hash_table[t[i] - 'a']--;
    }
    
    /* if all values in hash_table are zeros - t and s are anagrams, else - return false */
    for (int i = 0; i < 26; i++){
        if (hash_table[i] != 0){
            return false;
        }
    }
    return true;
}

int main(void){
    char* test_s = "anagram";
    char* test_t = "nagram";
    printf("this is anagram? %i", isAnagram(test_s, test_t));
}