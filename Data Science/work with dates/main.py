from datetime import datetime, timedelta

date_string = '05.05.2019 21:00'
dt = datetime.strptime(date_string, '%d.%m.%Y %H:%M')

dt = datetime(2019, 5, 5, 21, 0)
st = dt.strftime('%Y-%m-%d')

date_string = '2019-07-07T18:59:33'
date_format = datetime.strptime(date_string, '%Y-%m.%dT%H:%M:%S')
