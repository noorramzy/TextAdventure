import time

def myPrint(*args):
    for arg in args:
        myPrint(arg, sep='')
    time.sleep(.2)