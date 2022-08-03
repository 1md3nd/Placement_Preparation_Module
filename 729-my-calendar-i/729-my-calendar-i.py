class MyCalendar:

    def __init__(self):
        self.event = []
        

    def book(self, start: int, end: int) -> bool:
        for s, e in self.event:
            if s < end and start < e:
                return False
        self.event.append((start,end))
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)