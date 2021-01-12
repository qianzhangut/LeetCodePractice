## use lower()
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()
        
## use ord and chr
class Solution:
    def toLowerCase(self, str: str) -> str:
        return "".join([chr(ord(i)+32) if ord("A")<=ord(i)<=ord("Z") else i for i in str ])