import time, threading

def saySorry():
    print('[thread %s ]:Micheal is playing!' % threading.current_thread().getName())
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5000):
        t = threading.Thread(target=saySorry)
        t.start()