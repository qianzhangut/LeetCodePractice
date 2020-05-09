
#split
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t = s.split()
        return len(t[-1]) if len(t)>0 else 0

#strip	
class Solution:		
	def lengthOfLastWord(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		s = s[::-1].strip()
		return s.find(' ') if s.find(' ') != -1 else len(s)