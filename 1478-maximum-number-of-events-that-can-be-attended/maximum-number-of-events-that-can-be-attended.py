import heapq

class Solution:
    def maxEvents(self, events):
        events.sort()

        min_heap = []
        day = 0
        index = 0
        n = len(events)
        result = 0

        while index < n or min_heap:
            if not min_heap:
                day = events[index][0]
            while index < n and events[index][0] <= day:
                heapq.heappush(min_heap, events[index][1])
                index += 1
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)
            if min_heap:
                heapq.heappop(min_heap)
                result += 1
                day += 1

        return result