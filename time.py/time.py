import datetime
# i = datetime.datetime.today()
# # d = i.strftime("%X")
# i1 = input("enter a date: ")

t1 = datetime.timedelta(2022,3,28,14,4,50)
t2 = datetime.timedelta(2022,3,20,2,5,6)
t = t1 - t2

print(t)
