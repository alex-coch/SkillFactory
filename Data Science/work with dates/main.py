from datetime import datetime, timedelta

date_string = '05.05.2019 21:00'
dt = datetime.strptime(date_string, '%d.%m.%Y %H:%M')

dt = datetime(2019, 5, 5, 21, 0)
st = dt.strftime('%Y-%m-%d')

date_string = '2019-07-07T18:59:33'
date_format = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S')

dt_list = ['2019-07-07T18:59:06', '2019-07-07T19:00:02', '2019-07-07T19:01:04']
datetime_list = [datetime.strptime(i, '%Y-%m-%dT%H:%M:%S') for i in dt_list]
print(datetime_list)

datetime_list = [
    datetime(2019, 7, 7, 18, 59, 6),
    datetime(2019, 7, 7, 19, 0, 2),
    datetime(2019, 7, 7, 19, 1, 4)
]
report_seconds = [int(datetime.strftime(i, '%S')) for i in datetime_list]
total_time = sum(report_seconds)
# print()