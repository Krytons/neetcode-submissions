class Solution {
    /**
     * @param {string[]} operations
     * @return {number}
     */
    calPoints(operations) {
        let overallScore = 0;
        let records = [];
        let currentRecord = 0;

        for (let i = 0; i < operations.length; i++){
            let currentValue = operations[i];
            let newRecord;
            switch(currentValue){
                case '+':
                    newRecord = (Number(records[currentRecord - 2]) + Number(records[currentRecord - 1]));
                    overallScore += newRecord;
                    records.push(newRecord);
                    currentRecord++;
                    break;
                case 'D':
                    newRecord = (2*Number(records[records.length - 1]));
                    overallScore += newRecord;
                    records.push(newRecord);
                    currentRecord++;
                    break;
                case 'C':
                    newRecord = records.pop();
                    overallScore -= newRecord;
                    currentRecord--;
                    break;
                default:
                    newRecord = Number(currentValue);
                    overallScore += newRecord;
                    records.push(newRecord);
                    currentRecord++;
                    break;  
            }
        }

        return overallScore;
    }
}
