/**
 * @param {number} result
 * @return {string}
 */
 var countAndSay = function(n) {
    

    var recursive_say = function(result, number){
        
        let unique_value = result[0];
        let count = 0;
        ret_result = ""
        /* 111223334 */
        for (let i of result){
            if (i === unique_value){
                count++;
            }
            else{
                ret_result = ret_result + count.toString() + unique_value;
                unique_value = i;
                count = 1;
            }
        }
        ret_result = ret_result + count.toString() + unique_value;

        if (number === 0){
            return ret_result;
        }
        else{
            return recursive_say(ret_result, number - 1);
        }
    }

    if (n === 1){
        return "1";
    }
    else{
        return recursive_say("1", n - 2);
    }
 }

 let test_n = 9;
 console.log(`result of say function is ${countAndSay(test_n)}`)