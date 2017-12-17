from threading import Thread
import time

def test1(nums):
    nums.append(55)
    print('test1: nums =', nums)

def test2(nums):
    time.sleep(1)
    print('test2: nums =', nums)

if __name__ == "__main__":
    nums = [11, 22, 33, 44]
    t1 = Thread(target= test1, args=(nums,))
    t1.start()
    t2 = Thread(target= test2, args=(nums,))
    t2.start()