from datetime import datetime, timedelta

# 获取当前时间
now = datetime.now()
print(now)

# datetime类型转换为timestamp类型
dt = datetime(1995, 11, 15, 12, 12)  # create a datetime
dt2stamp = dt.timestamp()
print(dt2stamp)

# timestamp类型转换为datetime类型
t = 816408720.0
print(datetime.fromtimestamp(t))  # 本地时区时间
print(datetime.utcfromtimestamp(t))  # utc时区时间

# str类型转换为datetime类型
cs = datetime.strptime('1995-11-15 12:00:00', '%Y-%m-%d %H:%M:%S')
print(cs)

# datetime类型转换为str类型
now1 = datetime.now()
print(now1.strftime('%Y-%m-%d %H:%M:%S'))

# datetime的加减
now2 = datetime.now()
now2 = now2 + timedelta(days=5)  # 当前时间后的五天
print(now2)
