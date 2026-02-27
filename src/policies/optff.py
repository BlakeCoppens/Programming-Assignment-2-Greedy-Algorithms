## This is where we will write the OPTFF policy for cache.

def run_optff(k, requests):
    cache = []
    misses = 0
    
    for i, request in enumerate(requests):
        if request in cache:
            continue
        
        misses += 1
        if len(cache) < k:
            cache.append(request)
            continue
        
        #cache is full, evict the item that will be used farthest in the future
        farthest_index = -1
        evict_index = 0
        
        for index, item in enumerate(cache):
            next_i = None
            for j in range(i+1, len(requests)):
                if requests[j] == item:
                    next_i = j
                    break
            if next_i is None: # item is not used again, evict it
                evict_index = index
                farthest_index = float('inf')
                break
            if next_i > farthest_index:
                farthest_index = next_i
                evict_index = index
                
        cache.pop(evict_index)
        cache.append(request)
    return misses

#Note: This implementation of OPTFF is currently O(n^2), I believe there is a more efficent implementation.
# if you want feel free to take a crack at it.