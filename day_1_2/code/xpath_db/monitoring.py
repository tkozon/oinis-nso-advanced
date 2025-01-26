import tracemalloc
import time
import functools

def measure(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        fn_res = fn(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        _ss = tracemalloc.take_snapshot()
        size = 0
        memory_blocks = 0
        for _i in _ss.statistics('lineno'):
            size += _i.size
            memory_blocks += _i.count
        profile_details = {
            "func-name": fn.__name__,
            "memory-blocks": memory_blocks,
            "memory-usage": f"{size / 10 ** 6:.2f} MB",
            "time-taken": f"{time_taken:.2f} seconds"
        }
        print(profile_details)
        tracemalloc.stop()
        return fn_res

    return wrapper
