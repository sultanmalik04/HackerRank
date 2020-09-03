Read docs [Calendar module](https://docs.python.org/2/library/calendar.html#calendar.setfirstweekday)

## Python
```python
import calendar
M, D, Y = map(int, input().split())
day_no = calendar.weekday(Y, M, D)  # returns day no of week
weekdays = list(calendar.day_name) # returns day names in week
print(weekdays[day_no].upper())
```