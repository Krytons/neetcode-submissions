class Solution:
    def DFS(self, startCourse, visited, adj, courseList) -> bool:
        stack = [(startCourse, False)]
        path = set()

        while stack:
            course, processed = stack.pop()
            #Cycle detection
            if not processed and course in path:
                return False
            if course in visited:
                continue

            if processed:
                path.remove(course)
                visited.add(course)
                courseList.append(course)
            else:
                stack.append((course, True))
                path.add(course)
                if course in adj:
                    for prerequisite in adj[course]:
                        stack.append((prerequisite, False))

        return True
    
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites or len(prerequisites) == 0:
            return list(range(0, numCourses))

        adj = {}
        for index in range(0, numCourses):
            adj[index] = []
        for nextCourse, previousCourse in prerequisites:
            adj[nextCourse].append(previousCourse)
        
    
        visited = set()
        courseList = []
        notConnected = set()
        for course in range(0, numCourses):
            if course not in visited:
                result = self.DFS(course, visited, adj, courseList)
                if not result:
                    return []
        
        for notConnectedCourse in notConnected:
            if notConnectedCourse not in visited:
                courseList.append(notConnectedCourse)
        return courseList
            

    