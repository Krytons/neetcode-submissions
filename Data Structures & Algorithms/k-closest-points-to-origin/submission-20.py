def swapPosition(array, origin, destination):
    array[origin], array[destination] = array[destination], array[origin]

def euclideanCalculusFromOrigin(x, y):
    return (x ** 2) + (y ** 2);

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #STEP 0 -- Exit condition 
        if k == len(points):
            return points

        #STEP 1 -- Consider k as pivot, move it to the last element of the points list
        swapPosition(points, k, -1)

        #STEP 2 -- Execute a quick select logic
        continueCondition = True
        i = -1
        start = 0
        stop = len(points) - 1
        while continueCondition:
            #STEP 2.A -- Apply Lomuto
            pivot = points[stop]
            pivotValue = euclideanCalculusFromOrigin(pivot[0], pivot[1])
            for index in range(start, stop + 1):
                currentElement = points[index]
                elementValue = euclideanCalculusFromOrigin(currentElement[0], currentElement[1])
                if elementValue <=  pivotValue:
                    i += 1
                    if i != index:
                        swapPosition(points, index, i)
                    
            #STEP 2.B -- Evaluate result based on pivot position
            if i == k - 1 or i == k:
                continueCondition = False
            elif i < k - 1:
                start = i + 1
            else:
                start = 0
                stop = i - 1
                i = -1

        return points[:k]