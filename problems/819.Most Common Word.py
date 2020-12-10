
## use regex
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        import re
        paragraph = re.sub(r'[^\w\s]',' ',paragraph)
        par = paragraph.split()
        par = [i.lower()  for i in par if i.lower() not in banned]
        print(par)
        d = {}
        max = 0
        res = ''
        for i in par:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1
            if d[i]>max:
                max = d[i]
                res = i
        

        return res
        
        
## use isalnum
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        par = "".join([c.lower() if c.isalnum() else ' ' for c in paragraph]).split()
        par = [i for i in par if i not in banned]
        d = {}
        max = 0
        res = ''
        for i in par:
            if i not in d:
                d[i] = 1 
            else:
                d[i] += 1
            if d[i]>max:
                max = d[i]
                res = i
        

        return res 