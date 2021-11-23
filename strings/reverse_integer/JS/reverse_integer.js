/**
 * @param {number} x
 * @return {number}
 */
 var reverse = function(x) {
    let answer = 0;
    const max_answer = Math.floor(((2**31) - 1) / 10);
    const min_answer = Math.ceil(-(2**31) / 10);
    
    while(x !== 0){
      let last_digit = x % 10;
      console.log(`\nlast digit=${last_digit} answer=${answer}`);
      /* overflow check */
      if (answer > max_answer || (answer === max_answer && last_digit > 7)){
          return 0;
      }
      else if (answer < min_answer || (answer === min_answer && last_digit < -8)){
          return 0;
      }
      if (x >= 0) {
          x = Math.floor(x / 10);}
      else{
          x = Math.ceil(x / 10);
      }
      answer = answer * 10 + last_digit;
    }
    return answer;
};

let test_x = -123;
console.log(`before: ${test_x}\nafter:  ${reverse(test_x)}`);