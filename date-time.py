from datetime import datetime, timedelta
# dt = datetime.now()
# print(dt.strftime('%d.%m.%Y %H:%m'))
# print(dt.strftime('%Y-%m-%d'))

# import locale
# locale.setlocale(locale.LC_TIME, "sk_SK")
# print(dt.strftime('%A %d %B %Y'))

dt_today = datetime.now()
print(dt_today.strftime('%Y-%m-%d'))

dt_yesterday = dt_today - timedelta(days=1)
print(dt_yesterday.strftime('%Y-%m-%d'))
dt_30 = dt_today - timedelta(days=30)
print(dt_30.strftime('%Y-%m-%d'))

date_str = "01/01/25 12:10:03.234567"
date_dt = datetime.strptime(date_str, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)
