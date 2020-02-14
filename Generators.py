'''
mygenerator=(x*x for x in range(3))
for i in mygenerator:
    print(i)
    '''
'''
mygenerator=[x*x for x in range(3)]
for i in mygenerator:
    print(i,end='')
'''
'''

def mygen(x,y):
    while x<=y:
        yield x
        x+= 1 #fill generator object with 5 and 10.
g=mygen(5,10) # display all numbers in the generator.
for i in g:
    print(i,end=' ')
'''

define mygen():
    yield 'A'
    yield 'B'
    yield 'c'
    g=mygen()
#FINISH THIS CODE  AND WRITE EXPLANATION FOR 'YIELD' WHILST COMPARING IT WITH 'RETURN'FUNCTIONALITY.
    
