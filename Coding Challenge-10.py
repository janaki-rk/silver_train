# DAILY CODING CHALLENGE 10
# Question asked by: APPLE
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import threading
from time import sleep, time


# Step 1:Spin off a new thread on each function we want to delay,sleep the requested amount,
#        and then run the function.
class Scheduler:
    def __init__(self):
        pass

    def delay(self, f, n):
        def sleep_then_call(n):
            sleep(n / 1000)
            f()

        t = threading.Thread(target=sleep_then_call)
        print("result")
        t.start()

    def f(self):
        pass

#     Call

# Step 1(Alternative): Using Lists
class Scheduler:
    def __init__(self):
        self.fns = [] # tuple of (fn, time)
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000
            for fn, due in self.fns:
                if now > due:
                    fn()
            self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
            sleep(0.01)

    def delay(self, f, n):
        self.fns.append((f, time() * 1000 + n))