
import time

def timer(f):
    def wrapper(*args, **kwargs):
        start = time.clock()
        f(*args, **kwargs)
        end = time.clock()
        print ("Elapsed: %f" % (end-start))
    return wrapper

@timer
def gennums():
    [x**2 for x in range(2000)]

gennums()
