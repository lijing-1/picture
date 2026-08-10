from datetime import datetime, timedelta
now = datetime.now()
t1 = now + timedelta(hours=1)
t2 = now - timedelta(hours=1)
if now.hour <5:
    timestamp_sec = int(now.timestamp())
    print(f"时间早于5点，时间戳(秒): {timestamp_sec}")
if now.hour >5:
    print(f"-1h {t2}")
