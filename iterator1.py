a=[1,2,3,4,5,6,7,8,9,10]
b=[]
for i in a:
    if(i%2==0):
        b.append(i)
print(b)
x=iter(b)

print(next(x), end=' ')
print(next(x), end=' ')
print(next(x))