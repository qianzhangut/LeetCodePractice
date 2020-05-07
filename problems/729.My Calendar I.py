class MyCalendar:

    def __init__(self):
        self.record = []
        

    def book(self, start: int, end: int) -> bool:
        if len(self.record)==0:
            self.record.append((start, end))
            return True
        left, right = 0, len(self.record)-1
        while left<right:
            mid = left + (right - left)//2
            if self.record[mid][0]>=end:
                right = mid-1
            elif self.record[mid][1]<=start:
                left = mid+1
            else:
                return False
        if self.record[left][0]>=end:
            self.record.insert(left,(start, end))
            return True
        elif self.record[left][1]<=start:
            self.record.insert(left + 1 , (start, end))
            return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)