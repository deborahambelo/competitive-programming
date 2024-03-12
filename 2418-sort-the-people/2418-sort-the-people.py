class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dicts={}
        for i in range(len(heights)):
            dicts[heights[i]]=names[i]
        dicts=dict(sorted(dicts.items(),reverse = True))
        print(dicts)
        arr=[]
        for i in dicts:
            arr.append(dicts[i])
        return arr
            