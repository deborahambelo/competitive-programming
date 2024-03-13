class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        maximum_height = max(heights)
        count = [0] * (maximum_height + 1)
        for height in heights:
            count[height] += 1
        index = 0
        sorted_names = [""] * len(names)
        for height in range(maximum_height, -1, -1):
            if count[height] > 0:
                for _ in range(count[height]):
                    sorted_names[index] = names[heights.index(height)]
                    index += 1
                count[height] = 0
        
        return sorted_names
