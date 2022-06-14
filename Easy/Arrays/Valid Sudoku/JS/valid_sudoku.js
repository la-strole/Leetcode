/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {

/* prepare rows, columns, box arrays */
/*---------------------------------------------------------*/
  const rows = [];
  for (let i = 0; i < 9; i++){
    rows[i] = [];
    rows[i].length = 9;
    rows[i].fill(0);
  }

  const columns = []; // array of arrays of values 9x9
  for (let i = 0; i < 9; i++){
    columns[i] = [];
    columns[i].length = 9;
    columns[i].fill(0);
  }


  const boxes = []; // array of array of arrays of values 9x9x9
  for (let i = 0; i < 9; i++){
    boxes[i] = new Array(9);
    for (let j = 0; j < 9; j++){
      boxes[i][j] = [];
      boxes[i][j].length = 9;
      boxes[i][j].fill(0);
    }
  }

/*-----------------------------------------------------------*/

  for (let r = 0; r < board.length; r++){
    for (let c = 0; c < board[0].length; c++){

      let value = board[r][c];

      /* looking for value in row */
      if (value === '.'){
        continue;
      }

      value = parseInt(value) - 1;

      if (rows[r][parseInt(value)]) {
        return false;
      }
      else {
        rows[r][parseInt(value)] = 1;
      }

      /* looking for value in column */
      if (columns[c][parseInt(value)]) {
        return false;
      }
      else {
        columns[c][parseInt(value)] = 1;
      }

      /* looking for value in boxes */

      if (boxes[Math.floor(r / 3)][Math.floor(c / 3)][parseInt(value)]) {
        return false;
      }
      else {
        boxes[Math.floor(r / 3)][Mayh.floor(c / 3)][parseInt(value)] = 1;
      }
    }
  }
  return true;
};
