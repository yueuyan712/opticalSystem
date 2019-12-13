'''
import threading

def doSomthing(arg):
    print arg


t1 = threading.Thread(target=doSomthing, args=('123',))
t1.start()
'''