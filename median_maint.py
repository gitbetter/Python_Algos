# Median maintenance algorithm utilizing python's
# useful heapq library.

import heapq

def medians(l):
    medians = []

    h_low = []
    h_high = []

    for x in l:
        # Decide where new element should go
        if (len(h_high) == 0 and len(h_low) == 0) or x >= h_high[0]:
            heapq.heappush(h_high, x)
        elif x < h_high[0]:
            heapq.heappush(h_low, -x)

        #rebalance heaps
        heap_diff = len(h_low) - len(h_high)
        while heap_diff not in (0, 1, -1):
            if len(h_low) > len(h_high):
                heapq.heappush(h_high, -(heapq.heappop(h_low)))
            elif len(h_low) < len(h_high):
                heapq.heappush(h_low, -(heapq.heappop(h_high)))
            heap_diff = len(h_low) - len(h_high)

        # Append median element to list
        if len(h_low) < len(h_high):
            medians.append(h_high[0])
        elif len(h_low) == len(h_high) or len(h_low) > len(h_high):
            medians.append(-(h_low[0]))

    return medians

if __name__ == "__main__":
    nums = []
    with open("median.txt") as f:
        lines = f.readlines()
        for line in lines:
            nums.append(int(line.rstrip()))

    m = medians(nums)
    print(sum(m) % len(nums))
