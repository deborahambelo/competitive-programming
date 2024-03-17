class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        count = 0
        i = 0
        j = 0
        
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:  # Use <= instead of <
                count += 1
                i += 1  # Move to the next player
            j += 1  # Move to the next trainer
        
        return count
