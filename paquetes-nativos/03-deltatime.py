from datetime import datetime, timedelta

fecha1 = datetime(2019, 1, 1)
fecha2 = datetime(2019, 3, 1)

delta = fecha2 - fecha1

print(delta)

print("days", delta.days)
print("seconds", delta.seconds)
print("microseconds", delta.microseconds)
print("total_seconds()", delta.total_seconds())
