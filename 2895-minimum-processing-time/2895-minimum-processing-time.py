class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        tasks.sort(reverse=True)
        processorTime.sort()
        bs = len(tasks) // len(processorTime)
        subarrays = []
        for i in range(0, len(tasks), bs):
            sub = tasks[i:i+bs]
            subarrays.append(sub)

        current_max = float('-inf')
        for i in range(len(subarrays)):
            for j in range(len(subarrays[i])):  
                sum1 = subarrays[i][j] + processorTime[i]
                current_max = max(current_max, sum1)
        return current_max


# Example usage:
processorTime = [8, 10]
tasks = [2, 2, 3, 1, 8, 7, 4, 5]
sol = Solution()
print(sol.minProcessingTime(processorTime, tasks))  # Output should be 16

    