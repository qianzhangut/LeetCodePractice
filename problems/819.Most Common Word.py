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