'''class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        tasks.sort(reverse = True)
        processorTime.sort()
        bs = len(tasks) // len(processorTime)
        subarrays = [] 
        for i in range(0, len(tasks), bs):
            sub = tasks[i:i+bs]
            subarrays.append(sub)
        
        
        current_max = float('-inf')
        for i in range(len(subarrays)):
            for j in range(len(processorTime)):
                sum1 = subarrays[i][0] + processorTime[i]
                current_max = max(current_max,sum1)
        return current_max
    '''
class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        """
        processorTime.sort()
        tasks.sort(reverse=True)
        minimum_time = processorTime[0]
        for i in range(len(tasks)):
            minimum_time = max(minimum_time, processorTime[i//4] + tasks[i])

        return minimum_time
        
                    
            