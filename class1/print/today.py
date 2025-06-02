from datetime import datetime as dt, timezone

UTC = timezone.utc

now = dt.now(tz=UTC)

print(now.strftime("%Y-%m-%d"))
