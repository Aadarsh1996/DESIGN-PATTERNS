from typing import List

class Reusable:

    def test(self):
        print(f"Object created with id : {self}")

class ReusablePool:

    def __init__(self,size):
        self.size = size
        self.free = []
        self.in_use = []
        for i in range(0,size):
            self.free.append(Reusable())

    def acquire(self) -> Reusable:
        if len(self.free) <= 0:
            raise Exception("No object is free/available..")
        r = self.free[0]
        self.free.remove(r)
        self.in_use.append(r)
        return r

    def release(self,r: Reusable):
        self.in_use.remove(r)
        self.free.append(r)

pool = ReusablePool(2)
r = pool.acquire()
r2 = pool.acquire()

r.test()
r2.test()

pool.release(r)
r3 = pool.acquire()
r3.test()
#r4 =pool.acquire()
print(r)
print(r3)
print(r2)
#print(r4)


