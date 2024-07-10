import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapq.heapify(max_heap)
        count = 0
        while count != k:
            largest = -heapq.heappop(max_heap)
            print(largest)
            
            count+=1
        return largest
            
            
          