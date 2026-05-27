class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image is None or (len(image) -1 ) < sr or (len(image[0]) -1 ) < sc:
            return image

        maxRow = len(image) -1
        maxColumn = len(image[0]) -1
        stack = [(sr,sc)]
        startValue = image[sr][sc]

        while stack:
            currentRow, currentColumn = stack[-1]
            image[currentRow][currentColumn] = color
            
            #TOP Direction
            if (currentRow - 1) >= 0 and image[currentRow - 1][currentColumn] == startValue and image[currentRow - 1][currentColumn] != color:
                stack.append((currentRow - 1, currentColumn))
                continue;

            #BOTTOM Direction
            if (currentRow + 1) <= maxRow and image[currentRow + 1][currentColumn] == startValue and image[currentRow + 1][currentColumn] != color:
                stack.append((currentRow + 1, currentColumn))
                continue;

            #LEFT Direction
            if (currentColumn - 1) >= 0 and image[currentRow][currentColumn - 1] == startValue and image[currentRow][currentColumn -1] != color:
                stack.append((currentRow, currentColumn -1))
                continue;

            #RIGHT Direction
            if (currentColumn + 1) <= maxColumn and image[currentRow][currentColumn + 1] == startValue and image[currentRow][currentColumn + 1] != color:
                stack.append((currentRow, currentColumn +1))
                continue;
                
            #Remove from stack
            stack.pop()


        return image