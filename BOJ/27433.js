const fs = require("fs");
const input = fs.readFileSync('/dev/stdin').toString().trim();
const input_num = Number(input);

function solution(num) {
    if(num<=1) {
        return 1
    }
    else {
        return num * solution(num-1)
    }
};
console.log(solution(input_num));