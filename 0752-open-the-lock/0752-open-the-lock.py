from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def combos(lock):
            res = []

            for i in range(4):
                digit = str((int(lock[i])+1) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
                digit = str((int(lock[i])-1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i+1:])
            return res
        q = deque()
        q.append(["0000", 0]) # lock, no_turn
        visited = set(deadends)
        while q:
            lock, no_turns = q.popleft()
            if lock == target:
                return no_turns
            for i in combos(lock):
                if i not in visited:
                    visited.add(i)
                    q.append([i, no_turns+1])
        return -1
                