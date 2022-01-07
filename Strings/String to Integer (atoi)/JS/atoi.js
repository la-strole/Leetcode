/**
 * @param {string} s
 * @return {number}
 */
 var myAtoi = function(s) {
    let digit_expect = false;
    let positive = 1;
    let result = 0;
    const max_int = Math.floor(((2**31) - 1) / 10);
    const min_int = Math.ceil(-(2**31) / 10);
    for (let letter of s){
        if (!digit_expect){
            if (letter === ' '){
                continue;
            }
            else if (letter === '+'){
                digit_expect = true;
                continue;
            }
            else if (letter === '-'){
                digit_expect = true;
                positive = -1;
                continue;
            }
            else if (letter >= '0' && letter <= '9'){
                result += parseInt(letter);
                digit_expect = true;
                continue;
            }
            else{
                return 0;
            }
        }
        else{
            if (!(letter >= '0' && letter <= '9')){
                break;
            }
            else{
                number = parseInt(letter)
                if (positive == 1){
                    if (result > max_int || (result == max_int && number > 7)){
                        return 2**31 - 1;
                    }
                    else{
                        result = result * 10 + number;
                    }
                }
                else{
                    if (result < min_int || (result == min_int && number > 8)){
                        return -1 * 2**31;
                    }
                    else{
                        result = result * 10 - parseInt(letter);
                    }
                }
            }

        }
    }
    return result;
};

let tests = ["21474836460", "", "42", "-42", "+42", "  -42", "+-42", " +-42", "42somewords", "2147483648", "2147483647",
"-2147483648", "21474836480", "-214748364862", " ", "  0000000000012345678", "   -115579378e25"];

for (i of tests){
    console.log(`result for ${i} is ${myAtoi(i)}`);
}