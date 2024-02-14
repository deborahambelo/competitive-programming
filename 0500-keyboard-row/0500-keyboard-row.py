class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ls1=list("qwertyuiop")
        ls2=list("asdfghjkl")
        ls3=list("zxcvbnm")
        res=[]
        for k in words:
            w=k.lower()
            w=list(w)
            for i in w:
                if not(i in ls1):
                    break
            else:
                res.append(k)
            for i in w:
                if not(i in ls2):
                    break
            else:
                res.append(k)
            for i in w:
                if not(i in ls3):
                    break
            else:
                res.append(k)
        return res
                    
            