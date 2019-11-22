def gen():
    n=1
    print("printing n's value first time")
    yield  n
    n+=1

    print("printing n's second time")
    yield n
    n+=1

    print("printing n's value third time")
    yield n

a=gen()
print(next(a))
print(next(a))
print(next(a))

