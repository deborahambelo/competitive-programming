class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        i = 0
        j = len(skill) - 1
        skill.sort()
        target_sum = skill[i] + skill[j]
        chemistry_sum = 0

        while i < j:
            if skill[i] + skill[j] != target_sum:
                return -1
            chemistry_sum += skill[i] * skill[j]
            i += 1
            j -= 1
        
        return chemistry_sum

