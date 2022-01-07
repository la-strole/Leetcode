#include <stdio.h>

int isValidSudoku(int board[9][9], int boardRowSize, int boardColSize) {
    int rows[9][9]={0}; //rows[5][0] means whether number 1('0'+1) in row 5 has appeared.
	int cols[9][9]={0}; //cols[3][8] means whether number 9('8'+1) in col 3 has appeared.
	int blocks[3][3][9]={0};//blocks[0][2][5] means whether number '6' in block 0,2 (row 0~2,col 6~8) has appeared.
	for(int r=0;r<9;r++)    //traverse board r,c
		for(int c=0;c<9;c++)
			if(board[r][c]!='.'){   //skip all number '.'
				int number=board[r][c]-'1'; //calculate the number's index(board's number minus 1)
				if(rows[r][number]){
                    return 0;} //if the number has already appeared once, return false.
                else{
                    rows[r][number]++;
                }

				if(cols[c][number]){
                    return 0;}
                else{
                    cols[c][number]++;
                }
				if(blocks[r/3][c/3][number]){
                    return 0;}
                else{
                    blocks[r/3][c/3][number]++;
                }
			}
	return 1;
    }



int main(void){
    int test_board[9][9] = {{'8','3','.','.','7','.','.','.','.'},
                               {'6','.','.','1','9','5','.','.','.'},
                               {'.','9','8','.','.','.','.','6','.'},
                               {'8','.','.','.','6','.','.','.','3'},
                               {'4','.','.','8','.','3','.','.','1'},
                               {'7','.','.','.','2','.','.','.','6'},
                               {'.','6','.','.','.','.','2','8','.'},
                               {'.','.','.','4','1','9','.','.','5'},
                               {'.','.','.','.','8','.','.','7','9'}};

    
    
    printf("sudoku is valid: %i", isValidSudoku(test_board, 9, 9));
    
}