from datetime import datetime, timedelta
now = datetime.now()
t1 = now + timedelta(hours=1)
t2 = now - timedelta(hours=1)
if now.hour >5:
    print(f"+1h {t1}")
if now.hour >5:
    print(f"-1h {t2}")
