class Solution {

    sort(){

    }

    /**
     * @param {number[]} arr
     * @return {number[]}
     */
    replaceElements(arr) {
        let i,j,maxValueIndex = 0;
        let currentMaxValue;

        while(maxValueIndex < (arr.length -1)){
            currentMaxValue = null;
            j = maxValueIndex;
            i = maxValueIndex+1;
            for (i; i<arr.length; i++){
                let currentValue = arr[i];
                if(!currentMaxValue || currentValue >= currentMaxValue){
                    currentMaxValue = currentValue;
                    maxValueIndex = i;
                }
            }
            for (j; j < maxValueIndex; j++){
                arr[j] = currentMaxValue;
            }
            console.log('maxValueIndex: ', maxValueIndex);
        }


        arr[arr.length -1] = -1;
        return arr;
    }
}
