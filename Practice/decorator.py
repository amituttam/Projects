
import time

def timer(f):
    def wrapper(*args, **kwargs):
        start = time.clock()
        f(*args,**kwargs)
        end = time.clock()
        print "Total Time: %f" % (end-start)

    return wrapper

@timer
def listcomp(n):
    a = [x**2 for x in range(n)]

listcomp(1000)
