## This is where we will write the fifo policy for cache.

def run_fifo(k, requests):
    cache = []
    misses = 0
    for request in requests:
        if request in cache:
            continue
        misses +=1
        if len(cache) < k:
            cache.append(request)
        else:
            cache.pop(0)
            cache.append(request)
    return misses 