from datetime import date
dat = date.today()
data = f"{dat.day+2}/{dat.month}/{dat.year}"
print(data)