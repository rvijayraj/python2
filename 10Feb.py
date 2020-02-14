#SPLIT FUCTION:

#problem to be solved because input returned is Total:1 and Average:0.333 or input: 1,2,3.
'''
def calculate(lst):
    n=len(lst)
    sum=0
    for i in lst:
        sum=sum+i
        avg=sum/n
        return sum,avg 
print('Enter Numbers:')
lst=[int(x)for x in input().split()]
x,y=calculate(lst)
print("Total:",x)
print("Average:",y)

'''



#CORRECTED SYNTAX:

def calculate(lst):
    n=len(lst)
    sum=0
    for i in lst:
        sum=sum+i
        avg=sum/n
    return sum,avg # RETUN SHOULD BE OUTSIDE FOR LOOP:  
print('Enter Numbers:')
lst=[int(x)for x in input().split()]
x,y=calculate(lst)
print("Total:",x)
print("Average:",y)

# JUST BECAUSE RETURN IS INSIDE FOR LOOP WE ARE JUST GETTING ONLY SUM AS FIRST VALUE AND AVERAGE AS FIRST VALUE BY TOTAL NUM OF VALUES

