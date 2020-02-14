from salary import*
# calculate gross salary of an employeeby taking the basic
basic =float(input('Enter Basic Salary:'))
#calculate gross salary
gross=basic+da(basic)+hra(basic)
print('Your Gross Salary is:{:10.2f}'.format(gross))
#calculate net salary
net=gross-pf(basic)-itax(gross)
print("Your Net Salary is:{:10.2f}".format(net))

