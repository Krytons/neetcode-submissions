class Solution:
    def DFS(self, visited, adjList, initCourse) -> bool:
        path = set()
        stack = [(initCourse, False)]

        while stack:
            course, isAnalyzed = stack.pop()
            #STEP 1 -- Visited condition to avoid duplicate lookups
            if course in visited:
                continue

            #STEP 2 -- Loop detection
            if not isAnalyzed and course in path:
                return False

            #STEP 3 -- Prerequisites stack addition or visited addition
            if not isAnalyzed:
                stack.append((course, True))
                path.add(course)
                if course in adjList:
                    for prerequisite in adjList[course]:
                        stack.append((prerequisite, False))
            else:
                path.remove(course)
                if course not in visited:
                    visited.add(course)

        return True


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or len(prerequisites) == 0:
            return True

        adjList = {}
        for index in range(0, numCourses):
            adjList[index] = []
        for mandatoryCourse, nextCourse in prerequisites:
            adjList[mandatoryCourse].append(nextCourse)

        visited = set()
        for course in adjList:
            if course not in visited:
                if not self.DFS(visited, adjList, course):
                    return False
        return True



