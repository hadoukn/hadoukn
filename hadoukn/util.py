import time


def print_time(dt):
    """
    Returns milliseconds since the epoch
    """
    if dt:
        secs = time.mktime(dt.timetuple())
        return secs * 1000
    return None
