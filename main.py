import datetime
t1 = datetime.datetime.now().timestamp()
t2 = t1 % 14400

print(t1-t2)
value = datetime.datetime.fromtimestamp(cur_time)
print(value)