class Solution {
    /**
     * @param {number[]} students
     * @param {number[]} sandwiches
     * @return {number}
     */
    countStudents(students, sandwiches) {
        //STEP 1 -- Queue greedy count
        let studentsCount = [0, 0];
        students.forEach((student) => {
            studentsCount[student]++;
        });

        //STEP 2 -- Process the stack
        for (let i =0; i < sandwiches.length; i++){
            if(studentsCount[sandwiches[i]] === 0)
                return studentsCount[0] + studentsCount[1];
            else
                studentsCount[sandwiches[i]]--;
        }
        return 0;
    }
}
