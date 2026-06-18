from sortedcontainers import SortedList

class MyCalendar:
    
    def __init__(self):
        self.calendar = SortedList()

    def isIntesecating(self, index, startTime: int, endTime: int) -> bool:
        if index > len(self.calendar) - 1: 
            return False

        referenceStart, referenceEnd = self.calendar[index]
        return True if startTime < referenceEnd and endTime > referenceStart else False

    def book(self, startTime: int, endTime: int) -> bool:
        index = self.calendar.bisect_left((startTime,))

        if (index < len(self.calendar) and self.isIntesecating(index, startTime, endTime)) or (index > 0 and self.isIntesecating(index - 1 , startTime, endTime)):
            return False
        self.calendar.add((startTime, endTime))
        return True


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)