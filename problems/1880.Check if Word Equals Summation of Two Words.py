class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first = sum([(ord(f)-ord('a'))*(10**(len(firstWord)-1-i)) for i,f in enumerate(firstWord)])
        second =sum([(ord(f)-ord('a'))*(10**(len(secondWord)-1-i)) for i,f in enumerate(secondWord)])
        target =sum([(ord(f)-ord('a'))*(10**(len(targetWord)-1-i)) for i,f in enumerate(targetWord)])
        
        return first + second == target
        
        
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first = int("".join([str(ord(i)-ord('a')) for i in firstWord]))
        second =int("".join([str(ord(i)-ord('a')) for i in secondWord]))
        target =int("".join([str(ord(i)-ord('a')) for i in targetWord]))
        
        return first + second == target