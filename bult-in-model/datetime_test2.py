import re
from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    int
    ut = (int)(re.match('^UTC[+-]+0?(\d*):\d*', tz_str).groups(0)[0])
    stamp = dt.replace(tzinfo=timezone(timedelta(hours=ut))).timestamp()
    return stamp


s = to_timestamp('1995-11-15 12:12:12', 'UTC-3:00')
s1=816426732.0
print(datetime.fromtimestamp(s1))
print(s)
