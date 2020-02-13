Hours = float(input('Enter the amount of hours you worked this week'))
Wage = float(input('Enter your hourly wage'))
hours_fulltime = 40
hours_overtime = 60
rate_overtime = 1.5
rate_sovertime = 2.0
super_overtime = Hours - hours_overtime
overtime = Hours - hours_fulltime
if Hours <= hours_fulltime:
    print('You earned', '%0.2f' % (Hours * Wage))
elif (Hours > hours_fulltime) and Hours <= hours_overtime:
    print('You earned','%0.2f' % (rate_overtime * hours_fulltime + (Wage * rate_overtime) * overtime))
else:
    print('you eaned','%0.2f' % ((Wage * hours_fulltime) + (Wage * rate_overtime) * (hours_overtime - hours_fulltime) + (Wage * rate_sovertime) * super_overtime))