class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score_left = 0
        score_right = sum(nums)
        max_score = score_right
        best_indices = [0]
        for index, num in enumerate(nums):
            if num == 0:
                score_left += 1
            elif num == 1:
                score_right -= 1
            current_score = score_left + score_right
            if max_score == current_score:
                best_indices.append(index + 1)
            elif max_score < current_score:
                max_score = current_score
                best_indices = [index + 1]
        return best_indices
