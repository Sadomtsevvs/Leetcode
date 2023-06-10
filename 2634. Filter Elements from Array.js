/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let newArr = [];
    let i = 0;
    for (el of arr) {
        if (fn(el, i)) {
            newArr[i] = el;
            i++;
        }
    }
    return newArr;
};

function squareI(n, i) {
    return Math.pow(i, 2);
}

var a = [1,2,3,4,5,6,7,8,9]

console.log(filter(a, squareI))