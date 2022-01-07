#include <stdio.h>
#include <string.h>




int firstUniqChar(char * s){
    
    /* evevry element of hash array is letter[0|1|2_is_it_known|unique|duplicated, first_index_in_string_s] */
    unsigned int hash[26][2] = {0};
    
    // create hash table
    for (unsigned int index = 0; index < strlen(s); index++){
        unsigned char pos = (int) s[index] - 97; // ascii 'a' = 97
        if (hash[pos][0] == 2){ 
            continue;
        }
        else if (hash[pos][0] == 0){
            hash[pos][0] = 1; // unique from unknown
            hash[pos][1] = index; // position of potentionaly unique char
        }
       
        else if (hash[pos][0] == 1){
            hash[pos][0] = 2;
        }
    }
    
    // go trough hash table
    unsigned int result = strlen(s);
    for (unsigned char i = 0; i < 26; i++){
        if (hash[i][0] == 1){
            if (hash[i][1] < result){
                result = hash[i][1];
            }
        }
    }

    if (result == strlen(s)){
        return -1;
    }
    else{
        return result;
    }
}

int main(void){
    char *test_s = "aabb";
    
    
    printf("\nfirst unique char position is %i\n", firstUniqChar(test_s));
    
}