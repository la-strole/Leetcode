/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var rotate = function(matrix) {
    /* flip up and down */
    for (let row = 0; row < Math.floor(matrix.length / 2); row++){
      for (let column = 0; column < matrix[row].length; column++){
        let temp = matrix[row][column];
        matrix[row][column] = matrix[matrix.length - 1 - row][column];
        matrix[matrix.length - 1 - row][column] = temp;
      }
    }

    /* trans */
    for (let row = 0; row < matrix.length; row++){
      for (let column = row; column < matrix[row].length; column++){
        let temp = matrix[row][column];
        matrix[row][column] = matrix[column][row];
        matrix[column][row] = temp;
      }
    }
};

let test_matrix = [[1,2,3],[4,5,6],[7,8,9]];
console.log(test_matrix);
rotate(test_matrix);
console.log(test_matrix);
