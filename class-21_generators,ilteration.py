# for c in a:
#       print (a)
#Here a is an iterable.



def getNum (x):
    for i in range(x):
        yield i

seq = getNum (2)
print(seq.__next__())
print(seq.__next__())
print(seq.__next__())