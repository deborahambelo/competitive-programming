class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * (n+1)
        
        for book in bookings:
            b1, b2, b3 = book[0]-1, book[1], book[2]
            prefix[b1] += b3
            prefix[b2] -= b3
    
        prefix.pop()

        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        return(prefix)
                              
