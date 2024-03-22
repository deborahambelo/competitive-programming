class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_fruits = 0
        baskets = {}

        for right in range(len(fruits)):
            baskets[fruits[right]] = right

            if len(baskets) > 2:
                min_index = min(baskets.values())
                left = min_index + 1
                del baskets[fruits[min_index]]

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
