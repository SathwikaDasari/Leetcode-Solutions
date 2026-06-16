
class MyCalendarThree:
    def __init__(self):
        self.events = defaultdict(int)

    def book(self, start, end):
        self.events[start] += 1
        self.events[end] -= 1

        curr = 0
        k = 0

        for t in sorted(self.events):
            curr += self.events[t]
            k = max(k, curr)

        return k
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)