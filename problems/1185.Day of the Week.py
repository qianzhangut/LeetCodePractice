class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        import datetime
        
        t = datetime.datetime(year=year, month=month, day=day)
        return t.strftime('%A')