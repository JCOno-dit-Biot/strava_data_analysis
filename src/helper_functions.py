from datetime import datetime
import time

def datetime_to_unix_timestamp(date_str):
    """Converts a date string in YYYY-MM-DD format to a UNIX timestamp."""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return int(time.mktime(dt.timetuple()))