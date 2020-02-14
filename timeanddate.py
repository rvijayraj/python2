#printing basic time structure.
'''
import time
a=time.time()
c=time.localtime(a)
print(c)
'''
import time
epoch=time.time()
t=time.localtime(epoch)
#retrieve the date from structure t 
d=t.tm_mday
m=t.tm_mon
y=t.tm_year
print('current date is %d-%d-%d'%(d,m,y))
#retrieve the time structure from t
h=t.tm_hour
m=t.tm_min
s=t.tm_sec
print('current time is %d:%d:%d'%(h,m,s))
