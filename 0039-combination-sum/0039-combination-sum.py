class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def backtrack(cur_comb, c_sum, idx):
            if c_sum > target:
                return
            if c_sum == target:
                res.append(list(cur_comb))
                return
            for i in range(idx, len(candidates)):
                cur_comb.append(candidates[i])
                backtrack(cur_comb, c_sum+candidates[i], i)
                cur_comb.pop()
                
        backtrack([], 0, 0)
        return res
                
        
        