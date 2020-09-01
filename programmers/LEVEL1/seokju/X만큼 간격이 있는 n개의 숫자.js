function solution(x, n) {
    var answer = [];
    for (var i=0; i < n; i++) {
        answer.push(x + x*i);
    }
    return answer;
}

// 다른 풀이
function solution(x, n){
    var arr = Array(n).fill(x).map((v, i)=>(v + v* i))
    return arr
}