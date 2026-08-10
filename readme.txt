#从这个地址引用图片

from datetime import datetime, timedelta

# 获取系统当前时间
now = datetime.now()
print(f"系统当前时间: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 判断是否晚于早上5点
five_clock = now.replace(hour=5, minute=0, second=0, microsecond=0)

if now > five_clock:
    res_time = now + timedelta(hours=1)
    print(f"晚于5点，当前时间+1h：{res_time.strftime('%Y-%m-%d %H:%M:%S')}")
else:
    res_time = now - timedelta(hours=1)
    print(f"小于等于5点，当前时间-1h：{res_time.strftime('%Y-%m-%d %H:%M:%S')}")
