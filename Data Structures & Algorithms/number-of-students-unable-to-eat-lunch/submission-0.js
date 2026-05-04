class Solution {
    /**
     * @param {number[]} students
     * @param {number[]} sandwiches
     * @return {number}
     */
    countStudents(students, sandwiches) {
        //STEP 1 -- Queue greedy count
        let circularStudents = 0;
        let squareStudents = 0;
        students.forEach((student) => {
            if (student === 0)
                circularStudents++;
            else
                squareStudents++;
        });

        //STEP 2 -- Process the stack
        for (let i =0; i < sandwiches.length; i++){
            switch (sandwiches[i]){
                case 0:
                    if (circularStudents === 0)
                        i = sandwiches.length;
                    else
                        circularStudents--;
                    break;
                case 1:
                    if (squareStudents === 0)
                        i = sandwiches.length;
                    else
                        squareStudents--;
                    break;
            }
        }

        return squareStudents + circularStudents;
    }
}
