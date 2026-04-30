class Solution {

    sort(){

    }

    /**
     * @param {number[]} arr
     * @return {number[]}
     */
    replaceElements(arr) {
        let i = 0;
        let currentMaxValue = arr[arr.length-1];
        let newMaxValue;
        for(i = arr.length -1; i>=0; i--){
            if(arr[i] < currentMaxValue){
                arr[i] = currentMaxValue;
            }
            else if(arr[i] >= currentMaxValue){
                newMaxValue = arr[i];
                arr[i] = currentMaxValue;
                currentMaxValue = newMaxValue;
            }
        }


        arr[arr.length -1] = -1;
        return arr;
    }
}
