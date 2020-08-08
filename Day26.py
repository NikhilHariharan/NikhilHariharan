ret_date,ret_month,ret_year=[int(x) for x in input().split(' ')]
exp_ret_date,exp_ret_month,exp_ret_year=[int(x) for x in input().split(' ')]

if (ret_year,ret_month,ret_date)<=(exp_ret_year,exp_ret_month,exp_ret_date):
    print(0)

elif (ret_year,ret_month)==(exp_ret_year,exp_ret_month):
    print(15*(ret_date-exp_ret_date))

elif (ret_year==exp_ret_year):
    print(500*(ret_month-exp_ret_month))

else:
    print(10000)
