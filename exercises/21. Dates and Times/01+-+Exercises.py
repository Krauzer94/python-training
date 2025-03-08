# Question 1
# Write a function that, given an epoch timestamp, returns a `datetime` object set to the 
# beginning of that month (so midnight of the first day of the month).

from datetime import datetime

def beg(epts):
    dt = datetime.fromtimestamp(epts)
    beggining = dt.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    return beggining

ep_ts = 12345678.9
beg(ep_ts)  # Output: datetime.datetime(1970, 5, 1, 0, 0)

# Question 2
# Write a function that returns the difference in hours between two dates provided as 
# Python standard ISO formatted strings, rounded to the nearest hour. For simplicity, 
# assume that these dates do not contain fractional seconds.

# For example, given these two dates:
# '2001-01-01T13:50:23'
# and
# '2001-06-12T14:23:50'
# your result should be `3889` hours.

from datetime import datetime, timedelta

def t_dif(f_time, s_time):
    datetime_format = '%Y-%m-%dT%H:%M:%S'
    time1 = datetime.strptime(f_time, datetime_format)
    time2 = datetime.strptime(s_time, datetime_format)
    t_difference = time2 - time1
    return t_difference.total_seconds() / 3600

first_t = '2001-01-01T13:50:23'
second_t = '2001-06-12T14:23:50'

time_difference = t_dif(first_t, second_t)
print(f'\n  First time: {first_t}\n Second time: {second_t}\nDif in hours: {time_difference:.0f}')

# Question 3
# Write a function that can be used to consistently format `datetime` objects into strings 
# with some default format, but allows the caller to override the default format.

# For example, the default format could be `mm/dd/yyyy hh:mm:ss am/pm`, but your function 
# allows itself to be called with some argument that can override that format.

from datetime import datetime

def reformat(time_string, *, datetime_format='%m/%d/%Y %I:%M:%S %p'):
    return time_string.strftime(datetime_format)

# Example usage:
timing = datetime(2020, 2, 1, 13, 34, 5)
reformat(timing, datetime_format='%B %d, %Y')  # Output: 'February 01, 2020'
