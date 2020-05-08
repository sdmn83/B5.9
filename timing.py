import time
class Timing:
    def __init__(self, funct):
        self.runs = 10
        self.func_to_run = funct
    def __call__(self, *args, **kwargs):
        avg = 0
        for i in range(self.runs):
            t0 = time.time()
            self.func_to_run(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= self.runs
        fn = self.func_to_run.__name__
        print("[Timing] Среднее время выполнения %s за %s запусков: %.5f секунд" % (fn, self.runs, avg))
        return self.func_to_run(*args, **kwargs)

@Timing
def foo(par):
    for i in range(par):
        pass


foo(100000)