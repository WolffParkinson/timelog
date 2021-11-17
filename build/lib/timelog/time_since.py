import humanize
from datetime import datetime, timedelta

def time_since(dt:datetime)->str:
    output = ""
    now = datetime.utcnow()

    return humanize.naturaltime(now-dt)

    delta = now - dt

    if delta > timedelta(days=1):
        return "{} days".format(delta.days)
    elif delta > timedelta(hours=1):
        return "{} hours".format(round(delta.seconds/3600))
    elif delta > timedelta(minutes=1):
        return "{} mins".format(round(delta.seconds/60))
    elif delta > timedelta(seconds=0):
        return "Few seconds"
    else:
        return humanize

