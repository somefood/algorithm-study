var insertionSort = function(array){
    var i = 1, j, temp;
    for (i; i< array.length; i++){
        temp = array[i]; // 기존 수 임시보관
        for (j=i-1; j>=0 && temp < array[j]; j--){
            array[j+1] = array[j];
        }
        array[j + 1] = temp
    }
    return array
};

insertionSort([5, 6, 1, 2, 4, 3])