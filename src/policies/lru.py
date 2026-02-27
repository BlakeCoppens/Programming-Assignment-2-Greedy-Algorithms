## This is where we will write the lru policy for cache.

def run_lru(k, requests):
    cache = []
    misses = 0
    for request in requests:
        if request in cache:
            cache.remove(request)
            cache.append(request)
            continue
        misses +=1
        if len(cache) < k:
            cache.append(request)
        else:
            cache.pop(0)
            cache.append(request)
    return misses