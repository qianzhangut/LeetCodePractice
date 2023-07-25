class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        
        return  [i.strip()  for i in f'{separator}'.join(words).split(separator) if i]