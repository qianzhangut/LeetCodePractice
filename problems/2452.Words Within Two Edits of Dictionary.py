class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q in queries:
            for d in dictionary:
                cnt = 0
                for x, y in zip(q,d):
                    
                    if x!=y:
                        cnt +=1
                        if cnt >2:
                            break
                if cnt<=2:
                    ans.append(q)
                    break

        return ans
                