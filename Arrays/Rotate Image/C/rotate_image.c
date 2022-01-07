#include <stdio.h>

void rotate(int matrix[3][3], int matrixSize, int* matrixColSize){

    int matrixRowSize = 3;

    /* swap up -down */
    for (int row = 0; row < matrixRowSize / 2; row++){
        for (int column = 0; column < *matrixColSize; column++){
            int temp =  matrix[row][column];
            matrix[row][column] = matrix[matrixRowSize - 1 - row][column];
            matrix[matrixRowSize - 1 - row][column] = temp;
        }
    }

    /* trans */

    for (int row = 0; row < matrixRowSize; row++){
        for (int column = row; column < *matrixColSize; column++){
            int temp = matrix[row][column];
            matrix[row][column] = matrix[column][row];
            matrix[column][row] = temp;
        }
    }


}

int main(void){
    int test_matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {7, 8 ,9}};
    
    int size = 3;
    
    
    rotate(test_matrix, 9, &size);

    for (int i = 0; i < 3; i++){
        for (int j = 0; j < 3; j++){
            printf("%i ", test_matrix[i][j]);
        }
        printf("\n");
    }
}