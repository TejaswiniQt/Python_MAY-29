
# iterating

'''
dic1 = {1:'Green',2:'Red',3:'Blue',4:'Yellow'}
print(dic1)
for i in dic1.keys():
    if i == 2:
        del dic1[i]
print(dic1)
'''

# unpacking as arguments

'''
def fun(arg1='Hi',arg2='Welcome'):
    print(arg1 + " " + arg2)
    
    
list1 = ['Hello','World!']
fun(*list1)
'''


#Multiple keyword arguments

'''
def fun(**data):
    print(data)
    

fun(a=10,b=20,c=30)
fun()
fun(a=10)
'''

# iterating

'''

def fun(**data):
    for i,j in data.items():
        print('{}:{}'.format(i,j))

fun(a=10,b=20,c=30)
'''

# unpacking as arguments

'''
def fun(arg1='Orange',arg2='Banana',arg3='Apple'):
    print(arg1 + " " + arg2 + " " + arg3)

dic1 = {'arg1':'Green','arg2':'Red','arg3':'Yellow'}
fun(**dic1)
'''

'''
def fun(arg1='Orange',arg2='Banana',arg3='Apple'):
    print(arg1 + " " + arg2 + " " + arg3)

dic1 = {'arg1':'Green','arg':'Red','arg3':'Yellow'}
fun(**dic1)
'''

# abs()

'''
num1 = -0.6
print(abs(num1))

num2 = 5.3
print(abs(num2))

num3 = -5.90
print(abs(num3))

print(abs(2-9))

print(abs(10-5))
'''

# all()

list1 = ['True','True']
res = all(list1)
print(res)

list2 = ['True','True','False']
print(all(list2))

list3 = [10,20,0,40]
print(all(list3))


